

const CHARS: [char; 5] = ['=', '-', '0', '1', '2'];

fn int_to_base5(mut number: i32) -> String {
    // convert integer to funky base 5
    if number == 0 {
        return String::from("0");
    }

    let mut ret = String::from("");
    while number > 0 {
        let res = ((number + 2) / 5, (number + 2) % 5);
        ret = format!("{}{}", CHARS[res.1 as usize], ret);
        number = res.0
    }
    return ret;
}

fn base5_to_int(string: &str) -> i32 {
    // convert string back to integer
    let mut ret: i32 = 0;
    for digit in string.chars() {
        let value = CHARS
            .iter()
            .position(|&x| x == digit)
            .unwrap() as i32;
        ret = ret * 5 + (value - 2);
    }
    return ret;
}


fn main() {
    for x in 0..32 {
        let b5 = int_to_base5(x);
        let ret = base5_to_int(&b5);
        println!("{}: {}, {}", x, b5, ret);
    }
}
