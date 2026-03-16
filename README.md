# Repo général de la CDFR

Ce repo contient tous les codes ainsi que les cartes de la coupe de France.

## Instructions

1. Clonez ce dépôt :
   ```bash
   git clone --recurse-submodules git@github.com:robotronik/CDFR.git
   ```

**Ne pas oublier le flag --recurse-submodules !!**


## Composition

<pre>
CDFR/
├── informatique/
│   ├── Code General (Raspberry pi)
│   ├── Code Asservissement (stm32)
│   ├── Code Actionneur (Arduino)
│   └── Code Aruco OpenCV
└── electronique/
│   ├── shield Raspberry pi
│   ├── Carte Asservissement
│   └── Carte Actionneur
└── strategie
</pre>


## Correspondance code et carte

Raspberry pi (+ shield) -> Code Programme Robot  
Carte Asservissement -> Code Drive Control  
Carte Actionneur -> Code Actionneur   

## Description de chaque élément

### Code General (Raspberry pi)

Ce code gère la stratégie général. Pour cela, il analise les données par ses capteurs et envoie des commandes à la carte d'asservissement pour les déplacements et à la carte actionneur pour piloter les actionneurs. 

### Code Asservissement (stm32)

Ce code permet de gérer les déplacements du robot. Il déplace le robot vers la target donnée par le code général. Il reçoit les commandes du code général et envoie des commandes à la carte actionneur pour faire bouger les moteurs. Il reçoit aussi les données des capteurs de position pour faire du feedback et ajuster les déplacements.

### Code Actionneur (Arduino)

Ce code simple permet de controller les actionneurs à partir des commandes I2C.