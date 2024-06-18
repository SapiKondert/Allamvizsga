#include <stdio.h>
#include <iostream>
#include <stdlib.h> 
#include <fstream>
#include <time.h>
#include <random>
#include "bbs.h"
#include <winsock2.h>
#include <windows.h>

using namespace std;

void printBinary() {

	srand(time(0));
	ofstream o("out.txt");
	for (int i = 0; i < 2000000; i++) {
		o << rand() % 2;
	}
}


int main() {
	printBinary();
}