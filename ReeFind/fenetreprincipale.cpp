#include "fenetreprincipale.h"
#include "ui_fenetreprincipale.h"
#include "osfilesys.h"
#include "trie.h"
#include "renomme.h"
#include "rechercheretremplacer.h"
#include "QStringListModel"
#include "QFileSystemModel"
#include "QFileDialog"
#include "QMessageBox"
#include "QFile"
#include "QProgressDialog"
#include "QDesktopServices"
#include "QDirIterator"
#include "QFile"

QStringListModel *ModeleResultat = new QStringListModel();
QStringListModel *ModeleAIndexer = new QStringListModel();
QStringList      *DossierAIndexer = new QStringList();
QChar c;
bool age[5];
QTextDocument::FindFlags findOption = QTextDocument::FindFlag();
//QFileSystemModel *ModeleResultat = new QFileSystemModel();

FenetrePrincipale::FenetrePrincipale(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::FenetrePrincipale)
{
    ui->setupUi(this);

    //Onglet Recherche
    ui->R_ListViewResultat->setModel(ModeleResultat);
    ui->R_ListViewIndexage->setModel(ModeleAIndexer);

    QFile IndexFile("toIndex.txt");

    if(IndexFile.open(QIODevice::ReadOnly)){
        QString data;
        data = IndexFile.readAll();
        *DossierAIndexer = data.split("\r\n",Qt::SkipEmptyParts);
        updateDossierIndexer();
        IndexFile.close();
    }
    QObject::connect(ui->R_BoutonRecherche, SIGNAL(clicked()), this, SLOT(rechercher()));
    QObject::connect(ui->R_BoutonIndexage, SIGNAL(clicked()), this, SLOT(indexer()));
    QObject::connect(ui->R_BoutonAjouterDossier, SIGNAL(clicked()), this, SLOT(ajouterDossierIndexage()));
    QObject::connect(ui->R_BoutonRetirerDossier, SIGNAL(clicked()), this, SLOT(retirerDossierIndexage()));
    QObject::connect(ui->R_BoutonReinitialiserDossier, SIGNAL(clicked()), this, SLOT(reinitialiserDossierIndexage()));
    QObject::connect(ui->R_BoutonOuvrirDossier, SIGNAL(clicked()), this, SLOT(ouvrirDossier()));
    //Onglet Trier
    QObject::connect(ui->T_BoutonChoisir, SIGNAL(clicked()), this, SLOT(choisirDossierTrier()));
    QObject::connect(ui->T_BoutonSSD, SIGNAL(clicked()), this, SLOT(supprSousDossier()));
    QObject::connect(ui->T_BoutonTrier, SIGNAL(clicked()), this, SLOT(trier()));
    QObject::connect(ui->T_RadioButtonDecennie, SIGNAL(clicked()), this, SLOT(radioBoutonDecennie()));
    QObject::connect(ui->T_RadioButtonAnnee, SIGNAL(clicked()), this, SLOT(radioBoutonAnnee()));
    QObject::connect(ui->T_RadioButtonMois, SIGNAL(clicked()), this, SLOT(radioBoutonMois()));
    QObject::connect(ui->T_RadioButtonJour, SIGNAL(clicked()), this, SLOT(radioBoutonJour()));
    QObject::connect(ui->T_RadioButtonHeure, SIGNAL(clicked()), this, SLOT(radioBoutonHeure()));
    //Onglet Renommer
    QObject::connect(ui->N_BoutonChoisir, SIGNAL(clicked()), this, SLOT(choisirDossierRenommer()));
    QObject::connect(ui->N_BoutonRenommer, SIGNAL(clicked()), this, SLOT(renommer()));
    QObject::connect(ui->N_CheckBoxPerso, SIGNAL(clicked()), this, SLOT(radioBoutonPerso()));
    QObject::connect(ui->N_CheckBoxAnnee, SIGNAL(clicked()), this, SLOT(radioBoutonAnnee2()));
    QObject::connect(ui->N_CheckBoxMois, SIGNAL(clicked()), this, SLOT(radioBoutonMois2()));
    QObject::connect(ui->N_CheckBoxJour, SIGNAL(clicked()), this, SLOT(radioBoutonJour2()));
    QObject::connect(ui->N_CheckBoxHeure, SIGNAL(clicked()), this, SLOT(radioBoutonHeure2()));
    //Onglet Recherche & Remplacer
    QObject::connect(ui->C_BoutonChoisir, SIGNAL(clicked()), this, SLOT(choisirDossierRetR()));
    QObject::connect(ui->C_BoutonSuivant, SIGNAL(clicked()), this, SLOT(actionSuivant()));
    QObject::connect(ui->C_BoutonPrecedent, SIGNAL(clicked()), this, SLOT(actionPrecedent()));
    QObject::connect(ui->C_BoutonRemplacer, SIGNAL(clicked()), this, SLOT(remplacer()));
    QObject::connect(ui->C_BoutonRemplacerAll, SIGNAL(clicked()), this, SLOT(remplaceAll()));
    QObject::connect(ui->C_BoutonRemplacerAllInDoc, SIGNAL(clicked()), this, SLOT(remplaceAllInFile()));
    QObject::connect(ui->C_CheckBoxMot, SIGNAL(toggled(bool)), this, SLOT(updateFindOption()));
    QObject::connect(ui->C_CheckBoxCasse, SIGNAL(toggled(bool)), this, SLOT(updateFindOption()));
}
FenetrePrincipale::~FenetrePrincipale()
{
    delete ui;
}

/**
 * @brief FenetrePrincipale::rechercher
 */
void FenetrePrincipale::rechercher()
{
    if(!isIndexed()) {
        int reponse = QMessageBox::warning(this, tr("Attention"), tr("Il n'y a pas de fichier d'indexage.\nVoulez vous en réaliser un pour pouvoir effectuer une recherche?"), QMessageBox::Yes, QMessageBox::No);
        if(reponse == QMessageBox::Yes){
            indexer();
        } else {
            return;
        }
    }

    if(!ui->R_LineEditRechercher->text().isEmpty()){
        QStringList listResultat = recherche(ui->R_LineEditRechercher->text(),ui->R_CheckBoxCasse->isChecked());
        if(listResultat.length() != 0){
            ModeleResultat->setStringList(listResultat);
            ui->R_BoutonOuvrirDossier->setEnabled(true);
        } else {
            ModeleResultat->setStringList(listResultat);
            ui->R_BoutonOuvrirDossier->setEnabled(false);
            QMessageBox::information(this, tr("Pas de résultat"), tr("Pas de fichier ou dossier contenant \",Pas de fichier ou dossier contenant \"x\" trouvé")+ui->R_LineEditRechercher->text()+tr(" trouvé","Pas de fichier ou dossier contenant \"x\" trouvé"));
        }

    } else {
        QMessageBox::warning(this, tr("Attention"), tr("Veuillez remplir la barre de recherche avant de démarrer une recherche"));
        return;
    }
}

/**
 * @brief FenetrePrincipale::rechercher
 */
void FenetrePrincipale::indexer()
{

    if(ModeleAIndexer->rowCount() != 0){
        QStringList list = ModeleAIndexer->stringList();
        //QProgressDialog progress("Indexation...", "Arrêter ", 0, list.length(),this);
        //progress.setWindowModality(Qt::WindowModal);
        createIndex();
        for(int i = 0; i < list.length() ; i++){
            //progress.setValue(i);
            addIndex(list.at(i));
        }

        //progress.setValue(list.length());
    } else {
        QMessageBox::warning(this, tr("Attention"), tr("Veuillez selectionner un dossier avant de démarrer un indexage"));
        return;
    }
}


/**
 * @brief FenetrePrincipale::ajouterDossierIndexage
 */
void FenetrePrincipale::ajouterDossierIndexage()
{
    QString dossier = QFileDialog::getExistingDirectory(this);
    bool already = false;
    for(QString str : *DossierAIndexer){
        if(dossier.startsWith(str)){
            already = true;
        }
    }

    if(already){
        QMessageBox::information(this, tr("ReeFind"),tr("Le dossier \"","Le dossier \"x\" est déja inclue dans les dossiers à indexer")+dossier+tr("\" est déja inclue dans les dossier à indexer","Le dossier \"x\" est déja inclue dans les dossiers à indexer"));
        return;
    }

    for(int i = 0; i < DossierAIndexer->length();i++){
        if(DossierAIndexer->at(i).startsWith(dossier)){
            DossierAIndexer->removeAt(i);
            i--;
        }
    }
    DossierAIndexer->append(dossier);
    updateDossierIndexer();
    updateFichierIndexer();
}


/**
 * @brief FenetrePrincipale::retirerDossierIndexage
 */
void FenetrePrincipale::retirerDossierIndexage()
{
    QItemSelectionModel *selection = ui->R_ListViewIndexage->selectionModel();
    QModelIndexList listeSelections = selection->selectedIndexes();
    QString elementsSelectionnes;

    for (int i = 0 ; i < listeSelections.size() ; i++)
    {
        QVariant elementSelectionne = ModeleAIndexer->data(listeSelections[i], Qt::DisplayRole);
        DossierAIndexer->removeAll(elementSelectionne.toString());
    }
    updateDossierIndexer();
    updateFichierIndexer();
}

/**
 * @brief FenetrePrincipale::reinitialiserDossierIndexage
 */
void FenetrePrincipale::reinitialiserDossierIndexage()
{
    DossierAIndexer->clear();
    updateDossierIndexer();
    updateFichierIndexer();
}

/**
 * @brief FenetrePrincipale::ouvrirDossier
 */
void FenetrePrincipale::ouvrirDossier()
{
    QItemSelectionModel *selection = ui->R_ListViewResultat->selectionModel();
    QModelIndex indexElementSelectionne = selection->currentIndex();
    QString elementSelectionne = ModeleResultat->data(indexElementSelectionne, Qt::DisplayRole).toString();
    if(ui->R_CheckBoxOuvrir->isChecked()){
        if(!QDesktopServices::openUrl(QUrl::fromLocalFile(elementSelectionne.left(elementSelectionne.lastIndexOf('/'))))){
            QMessageBox::critical(this, tr("Échec"), tr("Échec de l'ouverture du fichier : \n")+elementSelectionne.left(elementSelectionne.lastIndexOf('/')));
        }
    } else if( !QDesktopServices::openUrl(QUrl::fromLocalFile(elementSelectionne))){
        if(!QDesktopServices::openUrl(QUrl::fromLocalFile(elementSelectionne.left(elementSelectionne.lastIndexOf('/'))))){
            QMessageBox::critical(this, tr("Échec"), tr("Échec de l'ouverture du fichier : \n")+elementSelectionne.left(elementSelectionne.lastIndexOf('/')));
        }
    }
}

/**
 * @brief FenetrePrincipale::updateDossierIndexer
 */
void FenetrePrincipale::updateDossierIndexer()
{
    ModeleAIndexer->setStringList(*DossierAIndexer);
}

/**
 * @brief FenetrePrincipale::updateDossierIndexer
 */
void FenetrePrincipale::updateFichierIndexer()
{
    QFile file("toIndex.txt");
    if(file.open(QIODevice::WriteOnly | QIODevice::Text)){
        QTextStream stream(&file);
        stream.setCodec("UTF-8");
        for(QString str : *DossierAIndexer){
            stream<<(str+"\n");
        }
    }
    file.close();
}


/**
 * @brief FenetrePrincipale::choisirDossierRenommer
 */
void FenetrePrincipale::choisirDossierTrier()
{
    QString dossier = QFileDialog::getExistingDirectory(this);
    ui->T_LineEditTrier->setText(dossier);
}


/**
 * @brief FenetrePrincipale::choisirDossierTrier
 */
void FenetrePrincipale::trier()
{
    if(ui->T_LineEditTrier->text().isEmpty()){
        QMessageBox::warning(this, tr("Attention"), tr("Veuillez remplir la champs de texte avant de démarrer le trie"));
        return;
    }
    QMap<QString, QStringList> categorie;
    if(ui->T_RadioButtonNom->isChecked()){
        categorie = trieNom(ui->T_LineEditTrier->text(),ui->T_SpinBoxNLettre->value(),ui->T_SpinBoxPlageLettre->value());
    } else if (ui->T_RadioButtonExtension->isChecked()) {
        categorie = trieExtension(ui->T_LineEditTrier->text(),ui->T_ComboBoxExtension->itemText(ui->T_ComboBoxExtension->currentIndex()).split(", *.",Qt::SkipEmptyParts));
    } else if (ui->T_RadioButtonPoid-> isChecked()){
        categorie = triePoid(ui->T_LineEditTrier->text(),ui->T_RadioButtonLineaire->isChecked(),ui->T_SpinBoxPlagePoid->value());
    } else if (ui->T_RadioButtonAge->isChecked()){
        categorie = trieAge(ui->T_LineEditTrier->text(),c);
    } else {
        QMessageBox::warning(this, tr("Aucune sélection"), tr("Aucun mode de trie n'est sélectionner"));
    }

    trie(categorie,ui->T_LineEditTrier->text(),ui->T_CheckBoxSD->isChecked(),ui->T_CheckBoxCP->isChecked(),ui->T_SpinBoxNbrElement->value());
}

/**
 * @brief FenetrePrincipale::choisirDossierRenommer
 */
void FenetrePrincipale::choisirDossierRenommer()
{
    QString dossier = QFileDialog::getExistingDirectory(this);
    ui->N_LineEditRenommer->setText(dossier);
}


void FenetrePrincipale::radioBoutonDecennie()
{
    c = 'd';
}

void FenetrePrincipale::radioBoutonAnnee()
{
    c = 'a';
}

void FenetrePrincipale::radioBoutonMois()
{
    c = 'm';
}

void FenetrePrincipale::radioBoutonJour()
{
    c = 'j';
}

void FenetrePrincipale::radioBoutonHeure()
{
    c = 'h';
}



/**
 * @brief FenetrePrincipale::choisirDossierTrier
 */
void FenetrePrincipale::renommer()
{
    if(ui->N_LineEditRenommer->text().isEmpty()){
        QMessageBox::warning(this, tr("Attention"), tr("Veuillez remplir la champs de texte avant de démarrer le renommage"));
        return;
    }
    QString prefix;
    if(ui->N_CheckBox_Prefixe){
        prefix = ui->N_LineEditPrefixe->text();
    } else {
        prefix = "";
    }

    QString suffix;
    if(ui->N_CheckBoxSufixe){
        suffix = ui->N_LineEditSufixe->text();
    } else {
        suffix = "";
    }
    renomme(ui->N_LineEditRenommer->text(),
            prefix,
            suffix,
            age,
            ui->N_LineEditPerso->text(),
            ui->N_ComboBoxExtension->itemText(ui->N_ComboBoxExtension->currentIndex()).split(", *.",Qt::SkipEmptyParts),
            ui->N_CheckBoxNomActuel->isChecked(),
            ui->N_CheckBoxNoSDir->isChecked());
}



void FenetrePrincipale::radioBoutonPerso()
{
    age[4] = ui->N_CheckBoxPerso->isChecked();
}

void FenetrePrincipale::radioBoutonAnnee2()
{
    age[0] = ui->N_CheckBoxAnnee->isChecked();
}

void FenetrePrincipale::radioBoutonMois2()
{
    age[1] = ui->N_CheckBoxMois->isChecked();
}

void FenetrePrincipale::radioBoutonJour2()
{
    age[2] = ui->N_CheckBoxJour->isChecked();
}

void FenetrePrincipale::radioBoutonHeure2()
{
    age[3] = ui->N_CheckBoxHeure->isChecked();
}

void FenetrePrincipale::supprSousDossier()
{

    if(ui->T_LineEditTrier->text().isEmpty()){
        QMessageBox::warning(this, tr("Attention"), tr("Veuillez remplir la champs de texte"));
        return;
    }

    QString dir = ui->T_LineEditTrier->text();
    QDirIterator it(dir, QDirIterator::Subdirectories);
    while(it.hasNext()){
        QString   fileName(it.next());
        QFileInfo f(fileName);
        if(f.isFile()){
            QString name = f.fileName();
            QFile::rename(fileName,dir+"/"+name);
        }
    }


    QDirIterator it2(dir);
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

void FenetrePrincipale::choisirDossierRetR(){
    QString dossier = QFileDialog::getExistingDirectory(this);
    ui->C_LineEditRetR->setText(dossier);
    init(ui->C_LineEditRetR->text(), false);
}

void FenetrePrincipale::actionSuivant(){

    if(ui->C_TextEditRetR->find(ui->C_LineEditTextToSearch->text(),findOption)){
        return;
    }
    save();
    while(nextFile()) {
        updateTextEdit();
        if(ui->C_TextEditRetR->find(ui->C_LineEditTextToSearch->text(),findOption)){
            return;
        }
    }
}

void FenetrePrincipale::actionPrecedent(){

    if(ui->C_TextEditRetR->find(ui->C_LineEditTextToSearch->text(),QTextDocument::FindBackward | findOption)){
        return;
    }
    save();
    while(previousFile()) {
        updateTextEdit();
        if(ui->C_TextEditRetR->find(ui->C_LineEditTextToSearch->text(),QTextDocument::FindBackward | findOption)){
            return;
        }
    }

}

void FenetrePrincipale::remplacer(){

    if(!ui->C_TextEditRetR->textCursor().hasSelection()){
        return;
    } else {
        ui->C_TextEditRetR->textCursor().removeSelectedText();
        ui->C_TextEditRetR->textCursor().insertText(ui->C_LineEditReplace->text());
    }
    save();
}

void FenetrePrincipale::remplaceAll(){
    goToFirstFile();
    do{
        updateTextEdit();
        while(ui->C_TextEditRetR->find(ui->C_LineEditTextToSearch->text(),findOption)){
            ui->C_TextEditRetR->textCursor().removeSelectedText();
            ui->C_TextEditRetR->textCursor().insertText(ui->C_LineEditReplace->text());
        }
        save();
    }while(nextFile());


}
void FenetrePrincipale::remplaceAllInFile(){
    updateTextEdit();
    while(ui->C_TextEditRetR->find(ui->C_LineEditTextToSearch->text(),findOption)){
        ui->C_TextEditRetR->textCursor().removeSelectedText();
        ui->C_TextEditRetR->textCursor().insertText(ui->C_LineEditReplace->text());
    }
    save();
}

void FenetrePrincipale::updateTextEdit(){
    QFile f(getActualFile());
    f.open(QIODevice::ReadOnly);
    QString text = f.readAll();
    ui->C_TextEditRetR->setPlainText(text);
    f.close();
}

void FenetrePrincipale::save(){
    QFile f(getActualFile());
    f.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream stream(&f);
    stream << (ui->C_TextEditRetR->toPlainText());
    f.close();
}

void FenetrePrincipale::updateFindOption(){
    findOption = QTextDocument::FindFlag();
    if(ui->C_CheckBoxCasse->isChecked() ){
        findOption |= QTextDocument::FindCaseSensitively;
    }

    if(ui->C_CheckBoxMot->isChecked() ){
        findOption |= QTextDocument::FindWholeWords;
    }
}


void FenetrePrincipale::on_C_LineEditRetR_textChanged(const QString &arg1)
{
    init(arg1,ui->C_CheckBoxSD);
}
