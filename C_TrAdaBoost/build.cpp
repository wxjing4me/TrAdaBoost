#include <fstream>
#include <iostream>
#include <string.h>

using namespace std;

const int MAX = 1000000;

int label;
double weight;
char line[MAX];

main(int argc, char* argv[]) {
	ifstream fin(argv[1]);   //文件读操作，读取 train.txt  
	ifstream fin0(argv[2]);  //文件读操作，读取 train_weight.txt    
	
	cout.precision(8);
	cout.setf(ios::fixed);   //用定点格式显示浮点数
	while (fin >> label) {
		fin0 >> weight;
		fin.getline(line, MAX);
		//if (weight < 0.1) continue;
		//if (weight > 2) weight = 2;
		if (label > 0) label = 1;
		if (label < 0) label = -1;
		cout << label << " cost:" << weight << ' ' << line << endl;
	}
	
	return 0;
}

