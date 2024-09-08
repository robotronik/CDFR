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
│   ├── librairie commune
│   └── simulation asservissement
└── electronique/
    ├── shield Raspberry pi
    ├── Carte Asservissement
    └── Carte Actionneur
</pre>


## Correspondance code et carte

Raspberry pi (+ shield) -> Code General  
Carte Asservissement -> Code Asservissement  
Carte Actionneur -> Code Actionneur   

## Description de chaque élément

### Code General (Raspberry pi)

Ce code gère la stratégie général. Pour cela, il analise le lidar et envoie des commandes à la carte d'asservissement pour les déplacements et à la carte actionneur pour piloter les actionneurs. 

### Code Asservissement (stm32)

Ce code permet de gérer les déplacements du robot. Il est composé de 3 grande partie.  
1. La première partie calcule la position du robot par odométire avec 2 roues codeuses
2. La deuxième partie gère l'asservisement en controllant les moteurs
3. La dernière partie s'occupe de la communication en I2C

### Code Actionneur (Arduino)

Ce code simple permet de controller les actionneurs à partir des commandes I2C.

### librairie commune

Elle permet de faire le lien entre le code Code Asservissement et le code de simulation asservissement ou le Code General.

### simulation asservissement

Permet de simuler l'asservissement et de faire des tests;

## Dependance

simulation asservissement à besoin de la librairie commune et du code Asservissement  
Code General du robot à besoin de la librairie commune

<pre>
simulation asservissement────────────┐
Code General (Raspberry pi)──────┐   │
                                 │   │
librairie commune <──────────────┘<──┤
Code Asservissement (stm32) <────────┘

</pre>
