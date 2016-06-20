#include <stdio.h>

int linear_combinations(int a, int b, int c, int d, int e, int f, int g, int h);

int main(){
	int count = 0;
	for(int a = 0; a <= 200; a++){
		for(int b = 0; b <= 100; b++){
			for(int c = 0; c <= 40; c++){
				for(int d = 0; d <= 20; d++){
					for(int e = 0; e <= 10; e++){
						for(int f = 0; f <= 4; f++){
							for(int g = 0; g <= 2; g++){
								for(int h = 0; h <= 1; h++){
									if(linear_combinations(a, b, c, d, e, f, g, h) == 200){
										count++;
										if(count % 100 == 0){
											printf("%d\n", count);
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	printf("%d\n", count);
}

int linear_combinations(int a, int b, int c, int d, int e, int f, int g, int h){
	return a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h;
}