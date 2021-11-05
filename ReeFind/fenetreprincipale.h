#ifndef FENETREPRINCIPALE_H
#define FENETREPRINCIPALE_H

#include <QWidget>

using namespace std;

namespace Ui {
class FenetrePrincipale;
}

class FenetrePrincipale : public QWidget
{
    Q_OBJECT

public:
    explicit FenetrePrincipale(QWidget *parent = nullptr);
    ~FenetrePrincipale();

private:
    Ui::FenetrePrincipale *ui;

    void updateDossierIndexer();

    void updateFichierIndexer();

public slots:
    void rechercher();

    void indexer();

    void ajouterDossierIndexage();

    void retirerDossierIndexage();

    void reinitialiserDossierIndexage();

    void ouvrirDossier();

    void choisirDossierTrier();

    void trier();

    void choisirDossierRenommer();

    void renommer();

    void radioBoutonDecennie();

    void radioBoutonAnnee();

    void radioBoutonMois();

    void radioBoutonJour();

    void radioBoutonHeure();

    void radioBoutonAnnee2();

    void radioBoutonMois2();

    void radioBoutonJour2();

    void radioBoutonHeure2();

    void radioBoutonPerso();

    void supprSousDossier();

    void choisirDossierRetR();

    void actionSuivant();

    void actionPrecedent();

    void updateTextEdit();

    void remplacer();

    void remplaceAll();

    void save();

    void remplaceAllInFile();

    void updateFindOption();
private slots:
    void on_C_LineEditRetR_textChanged(const QString &arg1);
};
#endif // FENETREPRINCIPALE_H
