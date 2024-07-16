package org.example;

public class User {
	private int age;
	
	User(){
		
	}
	
	void setAge(int age){
		try {
			this.age = age;
		}catch(IllegalArgumentException ex) {
			ex.printStackTrace();
		}
	}
		
}
