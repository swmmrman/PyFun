fn main() {
    let mut number = 0;
        for _ in 0..1_000_000_000 {
            number += 1;
            if number % 5000 == 0 {
                println!("{}", number)
            }
        }
    println!("{}", number);
}
