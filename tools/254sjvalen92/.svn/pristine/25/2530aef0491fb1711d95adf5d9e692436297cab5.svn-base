// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(INICIO)
	@KBD
	D=M
	@BLANCO
	D; JEQ
	@8193
	D=A
(NEGRO)
	D=D-1 
	@SCREEN 
	A=A+D 
	M=-1 // pinta negro
	@NEGRO
	D;JNE
	@INICIO
	D;JMP
(BLANCO)
	@8193
	D=A
(BLANCO_2)
	D=D-1
	@SCREEN
	A=A+D
	M=0 //pinta blanco
	@BLANCO_2
	D;JNE
	@INICIO
	D;JMP