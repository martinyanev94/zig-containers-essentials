// math_functions.h
#ifndef MATH_FUNCTIONS_H
#define MATH_FUNCTIONS_H

int add(int a, int b);
int subtract(int a, int b);
#endif
const std = @import("std");
const cImport = @cImport({
    @cInclude("math_functions.h");
});

pub fn main() void {
    const sum: i32 = cImport.add(5, 10);
    const difference: i32 = cImport.subtract(10, 4);
    
    std.debug.print("Sum: {}\nDifference: {}\n", .{sum, difference});
}
