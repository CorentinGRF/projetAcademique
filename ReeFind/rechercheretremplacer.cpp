#include "rechercheretremplacer.h"
#include "QFile"
#include "QFileInfo"
#include "QDirIterator"
#include "QWidget"
#include "QPlainTextEdit"
#include "osfilesys.h"

QList<QString>::iterator actual_file;
QList<QString>* listFile;
QList<QString>* ext = new QStringList("Toutes");

int init(QString dir,bool subDirect){
    if(!QFile::exists(dir)){
        return 1;
    } else if(!(new QFileInfo(dir))->isDir()){
        return 2;
    }
    QDirIterator::IteratorFlag mode;
    if(subDirect){
        mode = QDirIterator::Subdirectories;
    } else {
        mode = QDirIterator::NoIteratorFlags;
    }

    QDirIterator dir_it(dir,mode);
    listFile = new QStringList();

    while(dir_it.hasNext()){
        QString fileName = dir_it.next();
        QFileInfo f(fileName);
        if(isSelected(f)){
            listFile->append(fileName);
        }
    }
    if(listFile->count() == 0){
        return 3;
    } else {
       actual_file = listFile->begin();
       return 0;
    }
}

bool isSelected(QFileInfo fi){
    if(fi.isFile()){
        return ext->contains(fi.completeSuffix()) or ext->contains("Toutes");
    } else {
        return false;
    }
}


bool nextFile(){
    if(actual_file+1 != listFile->end()){
        actual_file ++;
        return true;
    } else {
        return false;
    }
}

bool previousFile(){
    if(actual_file != listFile->begin()){
        *actual_file --;
        return true;
    } else {
        return false;
    }
}

QString getActualFile(){
    return *actual_file;
}

void goToFirstFile(){
    actual_file = listFile->begin();
}
