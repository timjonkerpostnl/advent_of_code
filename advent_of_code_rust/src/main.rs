use std::fs::File;
use std::io::{BufRead, BufReader};

use rustc_hash::FxHashMap;

fn init_color_map() -> FxHashMap<String, u16> {
    let mut my_map = FxHashMap::default();
    my_map.insert("red".to_string(), 0);
    my_map.insert("blue".to_string(), 0);
    my_map.insert("green".to_string(), 0);
    my_map
}

fn parse_str_to_int(str_number: &str) -> u16 {
    match str_number.parse::<u16>() {
        Ok(parsed_number) => parsed_number,
        Err(_) => {
            panic!("{str_number} is not a valid number");
        }
    }
}

fn store_in_map(input_string: String) -> FxHashMap<String, u16> {
    let mut color_count = init_color_map();
    let components: Vec<String> = input_string
        .split(", ")
        .collect::<Vec<&str>>()
        .iter()
        .map(|s| s.to_string())
        .collect();
    for component in components {
        let count_color: Vec<&str> = component.trim().split(" ").collect();
        color_count.insert(count_color[1].to_string(), parse_str_to_int(count_color[0]));
    }
    color_count
}

fn extract_grabs(input_string: String) -> FxHashMap<String, u16> {
    let parts: Vec<&str> = input_string.split(':').collect();
    let grab_part = parts[1].to_string();
    let grabs: Vec<String> = grab_part
        .split(";")
        .collect::<Vec<&str>>()
        .iter()
        .map(|s| s.to_string())
        .collect();
    let mut maxima = init_color_map();
    let grab_results: Vec<FxHashMap<String, u16>> = grabs
        .iter()
        .map(|grab| store_in_map(grab.to_string()))
        .collect();

    for grab_result in grab_results {
        for (k, v) in grab_result {
            maxima.insert(k.clone(), std::cmp::max(maxima[&k], v));
        }
    }
    maxima
}

fn read_file(file_path: &str) -> Vec<String> {
    // Open the file in read-only mode and create a buffered reader
    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);

    // Create a vector to hold the lines of the file
    let mut lines = Vec::new();

    // Iterate over each line in the file and store it in the vector
    for line in reader.lines() {
        lines.push(line.unwrap());
    }
    lines
}

fn process_file_assignment1(file_path: &str) -> usize {
    let lines = read_file(file_path);
    let mut summed = 0;
    for (idx, line) in lines.iter().enumerate() {
        let max_grab_result = extract_grabs(line.to_string());
        if max_grab_result["red"] <= 12 && max_grab_result["green"] <= 13 && max_grab_result["blue"] <= 14 {
            summed += idx + 1;
        }
    }
    summed
}

fn process_file_assignment2(file_path: &str) -> u16 {
    let lines = read_file(file_path);
    let mut summed = 0;
    for line in lines {
        let max_grab_result = extract_grabs(line);
        let power = max_grab_result["red"] * max_grab_result["green"] * max_grab_result["blue"];
        summed += power;
    }
    summed
}

fn main() {
    let result1 = process_file_assignment1("/Users/timjonker/Documents/GitHub/advent_of_code/src/day2/input.txt");
    let result2 = process_file_assignment2("/Users/timjonker/Documents/GitHub/advent_of_code/src/day2/input.txt");
    println!("Result assignemtn1: {result1}, Result assignemtn2: {result2}");
}

#[cfg(test)]
mod tests {
    use super::*;
    use tracing_test::traced_test;

    #[test]
    #[traced_test]
    fn test_assignment_1() {
        let result = process_file_assignment1("/Users/timjonker/Documents/GitHub/advent_of_code/src/day2/test/test_input2.txt");
        assert_eq!(result, 8)
    }

    #[test]
    #[traced_test]
    fn test_assignment_2() {
        let result = process_file_assignment2("/Users/timjonker/Documents/GitHub/advent_of_code/src/day2/test/test_input2.txt");
        assert_eq!(result, 2286)
    }
}
