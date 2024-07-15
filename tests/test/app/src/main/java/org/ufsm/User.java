package org.ufsm;

public class User {
	private int idade;
	private double altura;
	private String nome;
	
	User(String nome, int idade, double altura){
		this.nome = nome;
		this.altura = altura;
		this.idade = idade;
	}
	
	String getNome() {
		return nome;
	}
	
	int getIdade() {
		return idade;
	}
	
	double getAltura(){
		return altura;
	}
}
