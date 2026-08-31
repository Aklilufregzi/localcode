import { describe, expect, it } from "vitest";
import { MinStack } from "./min-stack.ts";

describe("MinStack", () => {
  it("official example", () => {
    const st = new MinStack();
    st.push(-2);
    st.push(0);
    st.push(-3);
    expect(st.getMin()).toBe(-3);
    st.pop();
    expect(st.top()).toBe(0);
    expect(st.getMin()).toBe(-2);
  });

  it("min updates after pops", () => {
    const st = new MinStack();
    st.push(5);
    st.push(1);
    st.push(3);
    expect(st.getMin()).toBe(1);
    st.pop(); // removes 3
    expect(st.getMin()).toBe(1);
    st.pop(); // removes 1
    expect(st.getMin()).toBe(5);
    expect(st.top()).toBe(5);
  });

  it("duplicate minimums", () => {
    const st = new MinStack();
    st.push(2);
    st.push(2);
    st.push(3);
    st.pop();
    expect(st.getMin()).toBe(2);
    st.pop();
    expect(st.getMin()).toBe(2);
  });
});
