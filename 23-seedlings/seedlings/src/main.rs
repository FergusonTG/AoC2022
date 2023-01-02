#![allow(unreachable_code)]
#![allow(dead_code)]


use std::io;


type LineCol = (usize, usize);
type Grid = Vec::<Vec::<u8>>;


struct Elf {
    current: LineCol,
    proposed: LineCol
}

impl Elf {
    fn new(current_pos: LineCol) -> Elf {
        Elf {current: current_pos, proposed: current_pos}
    }

    fn neighbours(&self, grid: &Grid) -> Vec::<LineCol> {
        let mut ret = Vec::<LineCol>::new();
        for offset in vec![(0, 0), (0, 1), (0, 2), (1, 0),
                           (1, 2), (2, 0), (2, 1), (2, 2)].iter() {
            if (0 < offset.0 + self.current.0)
                && (self.current.0 + offset.0 < grid.len() + 1)
                && (0 < offset.1 + self.current.1)
                && (self.current.1 + offset.1 < (grid[self.current.0]).len() + 1) {

                ret.push((self.current.0 + offset.0 - 1, self.current.1 + offset.1 - 1));
            }
        }
        ret
    }

    fn propose(&mut self, grid: &Grid, directions: &[(usize, usize); 4]) -> Option<()> {

        let free_list: Vec::<LineCol> = self.neighbours(&grid)
            .iter()
            .filter(|loc| grid[loc.0][loc.1] != b'#')
            .map(|&loc| loc)
            .collect();

        for direction in directions {
            let count:usize = {
                if direction.0 == 0 && self.current.0 > 0 {
                    free_list.iter().filter(|loc| loc.0 + 1 == self.current.0).count()
                } else if direction.0 == 2 && self.current.0 + 1 < grid.len() {
                    free_list.iter().filter(|loc| loc.0 == self.current.0 + 1).count()
                } else if direction.1 == 0 && self.current.1 > 0 {
                    free_list.iter().filter(|loc| loc.1 + 1 == self.current.1).count()
                } else if direction.1 == 2 && self.current.1 + 1 < (grid[self.current.0]).len() {
                    free_list.iter().filter(|loc| loc.1 == self.current.1 + 1).count()
                } else {
                    0
                }
            };
            if count == 3 {
                self.proposed = (self.current.0 + direction.0 - 1, 
                                 self.current.1 + direction.1 - 1
                );
                return Some(());
            }
        }
        None
    }
}
        

struct ElfGrid {
    array: Vec::<u8>
}

struct GridIterator<'a> {
    grid: &'a Grid,
    current_line: usize,
    current_col: usize
}

impl <'a> GridIterator<'a> {
    fn new(grid: &Grid) -> GridIterator {
        GridIterator{ grid, current_line: 0, current_col: 0 }
    }
}

impl <'a> Iterator for GridIterator<'a> {

    type Item = LineCol;

    fn next(&mut self) -> Option<LineCol> {

        let mut ret: Option<LineCol> = None;

        loop {
            if self.current_line == self.grid.len() {
                break;  // returning None
            }

            if self.grid[self.current_line][self.current_col] == b'#' {
                // this will exit at the bottom of this loop
                ret = Some((self.current_line, self.current_col));
            }

            self.current_col += 1;
            if self.current_col == self.grid[self.current_line].len() {
                self.current_line += 1;
                self.current_col = 0;
            }

            if ret.is_some() {
                break;
            }
        }
        return ret;
    }
}


fn read_input() -> Grid {
    let mut grid = Grid::new();

    for line in io::stdin().lines() {
        let lineu8 = line.unwrap().chars().map(|c| c as u8).collect();
        grid.push(lineu8);
    }
    grid
}

fn main() -> io::Result<()> {

    let grid = read_input();

    println!("{} lines read", grid.len());
    
    let mut elves: Vec::<Elf> = Vec::new();

    for elf_pos in GridIterator::new(&grid) {
        elves.push(Elf::new(elf_pos));
    }

    let mut directions = [(0,1), (2,1), (1,2), (1,0)]; // north, south, west, east

    for mut elf in elves {
        if elf.propose(&grid, &directions).is_some() {
            println!("Elf {:?} proposes to move to {:?}", elf.current, elf.proposed);
        }
    }
    
    Ok(())
}
