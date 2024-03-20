package org.ufsm;

public class App {
	static User usuario;
	

    public static void main(String[] args) {
    	usuario = new User("Gabriel", 22, 180.0);
    	System.out.println(usuario.getNome());
    }
}
