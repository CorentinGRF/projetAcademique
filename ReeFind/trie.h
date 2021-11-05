#ifndef TRIE_H
#define TRIE_H

#include <QObject>
#include <QWidget>

using namespace std;

    QMap<QString, QStringList> trieNom(QString dir,int n, int k);

    QMap<QString, QStringList> trieExtension(QString dir,QStringList ext);

    QMap<QString, QStringList> triePoid(QString dir,bool Lin, double p);

    QMap<QString, QStringList> trieAge(QString dir,QChar c);

    void trie(QMap<QString, QStringList> cat,QString dir,bool sd,bool cp,int e);

#endif // TRIE_H
