#include "osfilesys.h"
#include <dirent.h>
#include <sys/types.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <stdbool.h>
#include <stdio.h>
#include <typeinfo>
#include <locale>
#include <algorithm>
#include <sstream>
#include <utility> // std::pair
#include <stdexcept> // std::runtime_error
#include <sstream> // std::stringstream
#include <cstring>
#include <QString>
#include <QDebug>
#include <QProgressDialog>
#include <QFile>
#include <QDirIterator>
/*

    Liste un répertoire
    retourne une liste de string

*/

/*

    Retourne un booléen qui dit si un chemin mène vers un dossier

*/
bool isDir( const char* pzPath )
{
    if ( pzPath == NULL) return false;

    DIR *pDir;
    bool bExists = false;

    pDir = opendir (pzPath);

    if (pDir != NULL)
    {
        bExists = true;
        (void) closedir (pDir);
    }

    return bExists;
}

/*

    Dit si pour un nom donné, ce nom correspond à un fichier

*/
bool fileExist(const string& name) {
    if (FILE *file = fopen(name.c_str(), "r")) {
        fclose(file);
        return true;
    } else {
        return false;
    }
}

/* says if index.csv exist or not*/
bool isIndexed() {
    return fileExist("index.csv");
}

/*

    créer les fichiers d'index et celui de ls_save
    index.csv contient toutes les info nécessaires

    ls_save sert juste pour nous pendant le developpement
    pour chercher des noms manuellement et faire des vérifications

*/
void indexFile(){
    if(!fileExist("index.csv")){
        ofstream file {"index.csv"};
    }
    /*if(!fileExist("ls_save.csv")){
        ofstream file {"ls_save.csv"};
    }*/
}

void addIndex(QString racine){
    string racine_to_index = racine.toStdString();
    indexFile();

    if(fileExist("index.csv") /*and fileExist("ls_save.csv")*/){

        QFile indexFile("index.csv");
        if(!indexFile.open(QIODevice::WriteOnly | QIODevice::Append | QIODevice::Text)){
            return;
        }
        QTextStream stream(&indexFile);
        stream.setCodec("UTF-8");

        QDirIterator it(racine, QDirIterator::Subdirectories);
        if(it.fileName() == ""){
            it.next();
        }
        while (it.hasNext()) {
            if((it.fileName() != ".") and (it.fileName() != "..")){
                stream << it.fileName()+","+it.filePath() + "\n";
            }
            it.next();
        }
        indexFile.close();
    }
}

/**
  createIndex index le dossier situé à racine_to_index
  et enregistre toutes les données dans un fichier index.csv
  de cette manière : <string>nom dossier/fichier;<string>chemin d'accès;

  complexité θ(n) où n est le nombre de sous dossiers et fichiers contenu dans le dossier à indexer

  À Faire :
    - le tri en direct pour la recherche
    - la création de mot clé pour la recherche
    - une gestion d'erreur et d'affichage de message
    - Attention ! chemin fait uniquement pour Windows !!! (avec le double back slash)

*/
void createIndex(){
    indexFile();
    string diskoupas;

    if(fileExist("index.csv")){

        ofstream indexFile;
        indexFile.open("index.csv");

        indexFile << "Nom,Chemin\n";

        indexFile.close();
    }
}

/**

    Ok donc
    donc dans l'index il faut enregistrer les noms dans un vector pour pouvoir les sort et faire de la dichotomie
    et il faut compter le nombre d'élément commençant pas une certaine lettre pour faire de l'interpolation manuelle :)

    sort est en θ(nlog(n))
    trouver la premiere occurence de P dans S en θ(|P| + |S|) dans le meilleur des cas sinon P*S dans le pire (p*s/2)
    origine : https://fr.wikipedia.org/wiki/Algorithme_de_Knuth-Morris-Pratt

    utiliser le long
    envoyer sur github

*/
vector<int> kmp_recherche(string P, string S, bool Casse)
{
    if(!Casse){
        for_each(S.begin(),S.end(), [](char & c){
            c = ::tolower(c);
        });
        for_each(P.begin(),P.end(), [](char & c2){
            c2 = ::tolower(c2);
        });
    }

    vector<int> res;

    int m = 0;
    int i = 0;

    while (S[m + i] != '\0' && P[i] != '\0'){
        if (S[m + i] == P[i])
        {
                              // Si on a encore une correspondance
            i++;              // alors on regarde la lettre suivante
        }
        else
        {
            // sinon
            m += 1;
            i = 0;
        }
    }

    //Quand on a fini de parcourir une des deux chaines
    if (P[i] == '\0')
    {
        //si la chaine P est finie alors on a trouvé une correspondance à la place m
        res.push_back(m);
        res.push_back(i);

        return res;
    }
    else
    {                    /* Sinon c'est qu'il n'existe pas de correspondance de
                      P dans S donc on renvoie un nombre impossible */
        res.push_back(-1);
        res.push_back(i);
        return res;    /* m est forcément le nombre de caractères de S, donc
                            m+1 est impossible. On pourrait aussi renvoyer -1 */
    }
}

/**

  be unicode proof (en gros ça supporte les accents quoi mais pas que, le chinois le russe bref les trucs comme ça)(Qstring!)

*/
QStringList recherche(QString toR,bool Casse){

    bool res;
    QStringList listResultat;
    QStringList listFichier;

    /*QFile file("index.csv");
    if (!file.open(QIODevice::ReadOnly)) {
        printf("test3");
    }

    while (!file.atEnd()) {
        printf("test2");
        listFichier.append(file.readLine());
    }*/
    QList<QStringList> indexData = readIndexCsv();

    Qt::CaseSensitivity casseSensibility;
    if(Casse){
        casseSensibility = Qt::CaseSensitive;
    } else {
        casseSensibility = Qt::CaseInsensitive;
    }

    //QProgressDialog progress("Indexation...", "Arrêter ", 0, listFichier.length(),window);
    //progress.setWindowModality(Qt::WindowModal);

    for(int k=0;k< indexData.length();k++){

        QString data = indexData.at(k).at(0);
        res = data.contains(toR,casseSensibility);

        if(res){
            listResultat <<indexData.at(k).at(1);
        }
        //progress.setValue(i);
    }
    //progress.setValue(listFichier.length());
    return listResultat;
}

/*

    readtest lis le csv index.csv et l'enregistre correctement dans une liste de pair de (string , liste de string)

*/
QList<QStringList> readIndexCsv(){
    QFile myFile("index.csv");

    if(myFile.open(QIODevice::ReadOnly)){
        QTextStream stream(&myFile);;
        stream.setCodec("UTF-8");
    }
    //ifstream myFile("index.csv");

    QList<QStringList> result;
    QString lineBrut;
    QStringList line;


    myFile.readLine();
    // Read data, line by line
    while(!myFile.atEnd()){

        lineBrut = myFile.readLine();
        lineBrut = lineBrut.remove("\r\n");
        line = lineBrut.split(',');
        result.append(line);
    }


        // Close file
    myFile.close();

    return result;
}


