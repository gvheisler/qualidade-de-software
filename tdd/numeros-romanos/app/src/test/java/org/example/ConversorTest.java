package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ConversorTest {
    @Test 
    void testaX(){
    	assertEquals(10, ConversorNumeros.converteRtoI("x"));
    }
    
    void testaIX(){
    	assertEquals(9, ConversorNumeros.converteRtoI("ix"));
    	assertEquals(9, ConversorNumeros.converteRtoI("IX"));
    }
}
