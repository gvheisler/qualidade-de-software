package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ConversorTest {
    @Test 
    void testaI(){
    	assertEquals(1, ConversorNumeros.converteRtoI("I"));
    }
    
    @Test 
    void testaV(){
    	assertEquals(5, ConversorNumeros.converteRtoI("V"));
    }
    
    @Test 
    void testaC(){
    	assertEquals(100, ConversorNumeros.converteRtoI("C"));
    }
    
    @Test 
    void testaII() {
    	assertEquals(2, ConversorNumeros.converteRtoI("II"));
    }
    
    @Test 
    void testaXXII() {
    	assertEquals(22, ConversorNumeros.converteRtoI("XXII"));
    }
    
    @Test 
    void testaIX() {
    	assertEquals(9, ConversorNumeros.converteRtoI("IX"));
    }
}
