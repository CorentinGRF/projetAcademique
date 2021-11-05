#include "renomme.h"
#include "QDirIterator"
#include "QDateTime"
#include "osfilesys.h"

void renomme(QString dir,QString pf,QString sf,bool* age,QString agePerso,QStringList ext,bool uNA,bool nSD){

    QDirIterator::IteratorFlag mode;
    if(nSD){
        mode = QDirIterator::NoIteratorFlags;
    } else {
        mode = QDirIterator::Subdirectories;
    }
    QString age_Format = "";
    if(age[4]){
        age_Format = agePerso;
    } else {
        if(age[0]){
            age_Format += "yyyy";
        }
        if(age[0] and (age[1] or age[2] or age[3])){
            age_Format += "-";
        }
        if(age[1]){
            age_Format += "MM";
        }
        if(age[1] and (age[2] or age[3])){
            age_Format += "-";
        }
        if(age[2]){
            age_Format += "dd";
        }
        if(age[2] and age[3]){
            age_Format += "-";
        }
        if(age[3]){
            age_Format += "hh";
        }
    }


    QDirIterator it(dir, mode);
    while(it.hasNext()){
        QString   fileName(it.next());
        QFileInfo f(fileName);
        if(f.isFile() and (ext.contains(f.completeSuffix().toLower()) or ext.contains("Toutes"))){
            QString path = fileName.left(fileName.lastIndexOf('/'))+"/";
            QString name = f.fileName().left(f.fileName().indexOf('.'));
            QString s_age = f.lastModified().toString(age_Format);
            QString extension = "."+ f.completeSuffix();
            if(uNA){
                QFile::rename(fileName,path+pf+name+s_age+sf+extension);
            } else {
                QFile::rename(fileName,path+pf+s_age+sf+extension);
            }
        }
    }
}
