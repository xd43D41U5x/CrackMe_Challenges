#include <iostream>

int main()
{
    std::string userName, passWord, result, shift;
    int number;
    int fudge = 7;

    std::cout << "Enter UserName\n";
    std::cin >> userName;

    std::cout << "Enter Number\n";
    std::cin >> number;

    std::cout << "Enter Password\n";
    std::cin >> passWord;

    char ch;
    number += fudge;

    for (size_t i = 0; i < userName.length(); i++)
    {
        ch = userName[i];
        //shift for lowercase
        if (ch >= 'a' && ch <= 'z') {
            result += (ch - 'a' + number) % 26 + 'a';
        }
        //shift for uppercase
        else if (ch >= 'A' && ch <= 'Z') {
            result += (ch - 'A' + number) % 26 + 'A';
        }
    }

    //std::cout << result << "\n";
    if (result == passWord) {
        std::cout << "Password is correct, ACCESS GRANTED!\n";
    }
    else {
        std::cout << "Password wrong, DENIED!\n";
    }
    system("pause");
}