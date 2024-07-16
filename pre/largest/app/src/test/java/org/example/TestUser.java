package org.example;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class TestUser {

	@Test
    void exceptionTesting() {
        User user = new User();
        Throwable exception = assertThrows(IllegalArgumentException.class, () -> user.setAge("23"));
        assertEquals("Age must be an Integer.", exception.getMessage());
    }

}
