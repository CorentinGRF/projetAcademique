#ifndef RECHERCHERETREMPLACER_H
#define RECHERCHERETREMPLACER_H


#include <QObject>
#include <QWidget>
#include <QPlainTextEdit>
#include <QFileInfo>

int init(QString dir, bool s);

bool isSelected(QFileInfo f);

bool suivant();

bool suivantInFile();

bool nextFile();

bool precedent();

bool precedentInFile();

bool previousFile();

void setTextEdit();

QString getActualFile();

int getActualCursor();

void goToFirstFile();
#endif // RECHERCHERETREMPLACER_H
