#ifndef OSFILESYS_H
#define OSFILESYS_H

#include <dirent.h>
#include <sys/types.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <QString>
#include <QDebug>

using namespace std;

vector<string> list_dir(const char *path);
bool isDir( const char* pzPath );
bool fileExist(const string& name);
bool isIndexed();
void indexFile();
void createIndex();
void addIndex(QString racine_to_index);
QStringList recherche(QString toR,bool Casse);
vector<int> kmp_recherche(string P, string S, bool noCasse);
QList<QStringList> readIndexCsv();

#endif // OSFILESYS_H
