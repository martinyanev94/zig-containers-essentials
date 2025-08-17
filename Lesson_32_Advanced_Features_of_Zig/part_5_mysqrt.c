// my_math.h
double my_sqrt(double x);
const std = @import("std");
extern "C" fn my_sqrt(x: f64) f64;

pub fn main() void {
    const number: f64 = 16.0;
    const result = my_sqrt(number);
    std.debug.print("Square root of {} is: {}\n", .{number, result});
}
