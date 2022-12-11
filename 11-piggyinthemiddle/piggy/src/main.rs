use std::collections::VecDeque;

struct Monkey<'a> {
    items: VecDeque<u32>,
    operation: &'a dyn Fn(u32) -> u32,
    test: &'a dyn Fn(u32) -> bool,
    iftrue: usize,
    iffalse: usize,
    inspected: u32
}

impl<'a> Monkey<'a> {
    fn inspect(&mut self) -> Option<(usize, u32)> {
        let mut worry = self.items.pop_front()?;
        worry = (self.operation)(worry);
        worry = worry / 3;
        self.inspected += 1;

        return Some((if (self.test)(worry) {
                         self.iftrue
                     } else {
                         self.iffalse
                     }, worry))
    }
}

fn main() {
    let mut monkeys: Vec<Monkey>  = Vec::new();
    monkeys.push(Monkey{
                items: VecDeque::from(vec![79, 98]),
                operation: &|w| w * 19,
                test: &|w| w % 23 == 0,
                iftrue: 2,
                iffalse: 3,
                inspected: 0
        });
    monkeys.push(Monkey{
                items: VecDeque::from(vec![54, 65, 75, 74]),
                operation: &|w| w + 6,
                test: &|w| w % 19 == 0,
                iftrue: 2,
                iffalse: 0,
                inspected: 0
        });
    monkeys.push(Monkey{
                items: VecDeque::from(vec![79, 60, 97]),
                operation: &|w| w * w,
                test: &|w| w % 13 == 0,
                iftrue: 1,
                iffalse: 3,
                inspected: 0
        });
    monkeys.push(Monkey{
                items: VecDeque::from(vec![74]),
                operation: &|w| w + 3,
                test: &|w| w % 17 == 0,
                iftrue: 0,
                iffalse: 1,
                inspected: 0
        });

    // for monkeynum in 0..monkeys.len() {
        // let monkey: &mut Monkey = &mut monkeys[monkeynum];
        for monkey in &mut monkeys {
        loop {
            match monkey.inspect() {
                Some((monkey2, item)) => {
                    let dest = &mut (monkeys[monkey2].items);
                    dest.push_back(item);
                    // monkeys[monkey2].items.push_back(item);
                    println!("{}, {}", monkey2, item);
                },
                None => {
                    break;
                }
            };
        };
    };
}
