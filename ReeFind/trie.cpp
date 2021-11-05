#include "trie.h"
#include "QFile"
#include "QDir"
#include "QDirIterator"
#include "osfilesys.h"
#include "QIODevice"
#include <QFileInfo>
#include <QDateTime>
#include <QtMath>

QMap<QString, QStringList> trieExtension(QString dir,QStringList ext){
    QMap<QString, QStringList> categorie;

    QDirIterator it(dir, QDirIterator::Subdirectories);
    while(it.hasNext()){
        QString   fileName(it.next());
        QFileInfo f(fileName);
        if(f.isFile() and (ext.contains(f.completeSuffix().toLower()) or ext.contains("Toutes"))){

            QString cat = f.completeSuffix().toLower();
            if(!categorie.contains(cat)){
                categorie[cat] = QStringList(fileName);
            } else {
                categorie[cat].append(fileName);
            }
        }
    }

    /*for(QString key : categorie.keys()){
        cout << ("key : " + key + "\n").toStdString();
        for(QString name: categorie.value(key)){
            cout << (name + "\n").toStdString();
        }
    }*/
    return categorie;
}


/*

    coucou hihihi x * 36 872 = 70 241 160

*/


QString getCategorie(QString mot, int n, int k){
    if(mot.size() < n){
        return QString::number(-1);
    }
    else{
        //cout << mot.toStdString();
        //cout << "\n";
        //cout << mot.toLower().at(n-1).toLatin1();
        //cout << "\n";
        return mot.left(n-1)+"_"+QString::number((mot.toLower().at(n-1).unicode()-'!')/k);
    }
}



QMap<QString, QStringList> trieNom(QString dir, int n, int k){

    QDirIterator it(dir, QDirIterator::Subdirectories);
    QMap<QString, QStringList> dico;


    /*
        On parcours le répertoire et on enregistre les noms des fichiers et leurs chemins
    */
    while (it.hasNext()) {

        QString   fileName(it.next());
        QFileInfo f(fileName);
        if(f.isFile()){

            QString cat = getCategorie(f.fileName(),n,k);

            if(!dico.contains(cat)){
                dico[cat] = QStringList(fileName);
            } else {
                dico[cat].append(fileName);
            }
        }
    }

//    qDebug() << dico;

    /*for(QString key : dico.keys()){
        cout << ("key : " + key + "\n").toStdString();
        for(QString name: dico.value(key)){
            cout << (name + "\n").toStdString();
        }
    }*/
    return dico;
}

QMap<QString, QStringList> trieAge(QString dir,QChar c){

    QDirIterator it(dir, QDirIterator::Subdirectories);
    /*
        On parcours le répertoire et on enregistre les noms de fichiers dans
    */
    QString formaDate;
    switch(c.toLatin1()){
    case 'd':
        formaDate = "yyyy";
        break;
    case 'a':
        formaDate = "yyyy";
        break;
    case 'm':
        formaDate = "yyyy-MM";
        break;
    case 'j':
        formaDate = "yyyy-MM-dd";
        break;
    case 'h':
        formaDate = "yyyy-MM-dd-hh";
        break;
    default:
        formaDate = "yyyy";
        break;
    }

    QMap<QString, QStringList> dico;

    while (it.hasNext()) {

        QString   fileName(it.next());
        QFileInfo f(fileName);
        if(f.isFile()){
            QFileInfo fi(fileName);
            QDateTime date = fi.lastModified();
            QString cat;
            if(c != 'd'){
                cat = date.toString(formaDate);
            } else {
                cat = date.toString(formaDate).left(3)+"x";
            }
            if(!dico.contains(cat)){
                dico[cat] = QStringList(fileName);
            } else {
                dico[cat].append(fileName);
            }
        }
    }



    /*for(QString key : dico.keys()){
        cout << ("key : " + key + "\n").toStdString();
        for(QString name: dico.value(key)){
            cout << (name + "\n").toStdString();
        }
    }*/
    return dico;
//    qDebug() << dico;
    return dico;
}

QMap<QString, QStringList> triePoid(QString dir, bool lin, double p){


    QDirIterator it(dir, QDirIterator::Subdirectories);
    QMap<QString, QStringList> dico;
    /*
        On parcours le répertoire et on enregistre les noms des fichiers et leurs chemins
    */
    while (it.hasNext()) {

        QString   fileName(it.next());
        QFileInfo f(fileName);
        QString cat;
        if(lin){
            qint64 pcat = f.size()/int(p*qPow(2,20));
            cat = QString::number(pcat);
        } else {
            qint64 pcat = int(qLn(f.size())/p);
            cat = QString::number(pcat);

        }
        if(f.isFile()){
            if(!dico.contains(cat)){
                dico[cat] = QStringList(fileName);
            } else {
                dico[cat].append(fileName);
            }
        }
    }

    /*for(QString key : dico.keys()){
        cout << ("key : " + key + "\n").toStdString();
        for(QString name: dico.value(key)){
            cout << (name + "\n").toStdString();
        }
    }*/
    return dico;
}

void trie(QMap<QString, QStringList> categorie,QString dir,bool sd,bool cp,int e){

    QDir directory(dir);
    for(QString key : categorie.keys()){
        if(!sd){
            QString path = key;
            if(!directory.exists(key) and categorie.value(key).count()>=e){
                directory.mkpath(key);
            } else if ((categorie.value(key).count()<e) and !directory.exists("autres")){
                path = "autres";
                directory.mkpath("autres");
            } else if((categorie.value(key).count()<e)){
                path = "autres";
            }
            for(QString name: categorie.value(key)){
                QFileInfo fi(name);
                if(!cp) {
                    QFile::rename(name,dir+"/"+path+"/"+fi.fileName());
                } else {
                    QFile::copy(name,dir+"/"+path+"/"+fi.fileName());
                }
            }
        } else {

            QMap<QString, QStringList> listPath;
            for(QString name: categorie.value(key)){
                QFileInfo fi(name);
                listPath[fi.filePath().left(fi.filePath().lastIndexOf('/'))].append(name);
            }


            /*cout << ("Key : " + key + "\n").toStdString();
            cout << "------------------\n";
            for(QString k: listPath.keys()){
                cout << ("DirectoryKey : " + k + "\n").toStdString();
                for(QString n: listPath.value(k)){
                    cout << (n + "\n").toStdString();
                }
            }*/

            for(QString keyDirectory : listPath.keys()){
                //cout << "----------------\n";
                //cout << (keyDirectory+"\n").toStdString();
                QDir d(keyDirectory);
                QString path = key;
                if(!d.exists(key) and listPath.value(keyDirectory).count()>=e){
                    d.mkpath(key);
                    path = key;
                } else if ((listPath.value(keyDirectory).count()<e) and !d.exists("autres")){
                    d.mkpath("autres");
                    path = "autres";
                    //cout << "lol2\n";
                } else if ((listPath.value(keyDirectory).count()<e)){
                    path = "autres";
                    //cout << "lol3\n";
                }
                for(QString name: listPath.value(keyDirectory)){
                    QFileInfo fi(name);
                    if(!cp) {
                    } else {
                        QFile::copy(name,keyDirectory+"/"+path+"/"+fi.fileName());
                    }
                }
            }
        }
    }
    QDirIterator it(dir);
    while(it.hasNext()){
        if(it.fileInfo().isDir()){
            QString name = it.next();
            QDir d(name);

            if(d.isEmpty(QDir::Files)){
                d.removeRecursively();
            }
        } else {
            it.next();
        }
    }
}
