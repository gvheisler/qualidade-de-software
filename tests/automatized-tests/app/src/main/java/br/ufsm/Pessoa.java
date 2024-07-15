package br.ufsm;

public class Pessoa {
	private int age;
	private String name;
	
	Pessoa(int age, String name){
		this.age = age;
		this.name = name;
	}
	
	int getIdade() {
		return this.age;
	}
	
	String getNome() {
		return this.name;
	}
	
	
}
