void *malloc(size_t size);
struct Foo *do_a_thing(void) {
    char *ptr = malloc(1234);
    if (!ptr) return NULL;
    return ptr;
}
const std = @import("std");

extern fn malloc(size: usize) ?[*]u8;

pub fn allocate() ?*Foo {
    const ptr = malloc(1234) orelse return null;
    return ptr; // Safe and straightforward
}
