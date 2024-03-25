package org.example;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class LargestTest {

	@Test
	void test1() {
		int[] vet = {7, 8, 9};
		assertEquals(9, Largest.largest(vet));
	}
	
	@Test
	void test2() {
		int[] vet = {8, 9, 7};
		assertEquals(9, Largest.largest(vet));
	}
	
	@Test
	void test3() {
		int[] vet = {9, 7, 8};
		assertEquals(9, Largest.largest(vet));
	}
	
	@Test
	void test4() {
		int[] vet = {1};
		assertEquals(1, Largest.largest(vet));
	}
	
	@Test
	void test5() {
		int[] vet = {-9, -8, -7};
		assertEquals(-7, Largest.largest(vet));
	}
}
