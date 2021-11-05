#include <QApplication>
#include <fenetreprincipale.h>
#include "osfilesys.h"
#include "trie.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    FenetrePrincipale fenetre;
    fenetre.show();
    return app.exec();

}


