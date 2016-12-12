#Le fonctionnement du site

##Prérequis

Tout d'abord pour pouvoir modifier le site web de l'équipe il faut :
  * avoir un compte github (ça prend 2 sec !)
  * s'affilier au groupe meom-group (Julien envoie l'invitation)
  * avoir les droits d'édition sur le dossier https://github.com/meom-group/meom-group.github.io (Julien envoie l'autorisation)

Ces deux dernières étapes sont en fait facultatives, n'importe qui peut proposer des modifications, les éditeurs se réservent ensuite le droit de les accepter (merge) ou non. Mais, pour les gens de l'équipe c'est quand même ùieux si vous faites partie du groupe meom !
 
Ensuite, deux solutions :
  * soit on modifie en ligne les fichiers présents dans ce repertoire afin de modifier le site (en cliquant sur le nom du fichier en question puis sur l'icone crayon "edit this file")
  * soit en téléchargeant une copie de tout le répertoire sur votre ordinateur, en local. Cela permet d'ajouter des fichiers et images plus facilement. (procédure ci-dessous)


##Modifications en local

La première fois, il faut d'abord "cloner" le répertoire, c'est-à-dire le télécharger en local :


```bash
git clone https://github.com/meom-group/meom-group.github.io.git
```

Un répertoire meom-group.github.io est ainsi créé.
On peut alors modifier les fichiers ou en ajouter.
Pour transmettre les modifs effectuées, 3 lignes de code sont nécessaires :


```bash
git add .
git commit -m "commentaire à joindre aux modifs"
git push
```

Avant de faire les prochaines modifs, pour prendre en compte celles qui on été faites entre-temps par d'autres personnes, une mise à jour est nécessaire :


```bash
git pull
```


##Différents types de pages :

  * page en html (ex: index.html)
  * page en markdown : c'est du html simplifié, (ex: nemo.md) pour pas s'ennuyer avec toutes les balises et syntaxes rébarbatives, la mise en page est faite dans un fichier à part, le layout (ex _layout/default.html)
  * les includes : ce sont des éléments qui se répetent dans toutes ou quelques pages comme l'en-tête, le menu de navigation ou le bas de page, on les trouve dans le répertoire _includes (ex: footer.html)
  * les fichiers en .yml : ils permettent de séparer encore une fois le contenu de la forme. Ils sont appellés dans les fichiers html par l'intermédiaire d'une boucle. A chaque fois qu'on rajoute des informations dans ce fichier yml, cela rajoute du contenu dans la page html

##Architecture du site :

Voici la correspondance entre les pages du site et les fichiers dans le dossier meom-group.github.io :

  * page d'accueil : index.html = carousel + welcome (= petit texte + icones)
  * page About : about/index.html
  * page People : people/index.html 
  * page Projects : projects/index.html
  * pages projets individuels : projects/sobums.md
  * page Code : code.md
  * page Data : data.md
  * page Publications : publications/index.html
  * page Job Offers : jobs.md
  * page News : blog/index.html
  * page Contact : contact/index.html
  * pages scientifiques :
    * unravel.md
    * forecast.md
    * climate.md
    

#Quelques actions de mises à jour qui risquent de revenir régulièrement

##Rajouter une image dans le carousel :

  * dans _includes/carousel.html :  rajouter ou modifier le nombre d'images

```html
    <li data-target="#carousel-generic" data-slide-to="4"></li>
```


  * dans _data/carousel.yml : rajouter un paragraphe 


```html
    - title :
      pic : assets/img/carousel/chaos3.png
      picg : assets/img/carousel/chaos3g.png
      picm : assets/img/carousel/chaos3m.png
      pics : assets/img/carousel/chaos3s.png
      text : Quantifying chaos and uncertainties in the ocean evolution
      link : forecast
      colorf : black
      colorb : white
```


dans lequel il faut donner le nom des 4 images (tailles 2052x340, 1000x340, 500x340, 250x340) , le texte, un lien vers lequel on accèdera en cliquant sur le "Read more", la couleur du texte et la couleur en fond du texte.

  * dans assets/img/carousel : déposer les images 
  
##Rajouter une nouvelle page scientifique à laquelle on accède via une image du carousel

  * faire les étapes du paragraphe précédent
  * créer une page markdown comme :
  

```html
---
layout: pagemd
title: Exploring the ocean fine scale dynamics
permalink: /unravel/
prevtext: About the MEOM team
prevlink:
nextext: Quantifying choas and uncertainties in the ocean evolution
nextlink: forecast
---



*Fine scale* ocean dynamics plays a key role in the climate machinery through various scale interaction mechanisms. Fine-scale ocean dynamics refer to ocean physical processes occuring at scales smaller than 200km, in the open ocean. This includes a fraction of *mesoscale* processes, with scales close to the first internal Rossby radius (20 to 200km). At mesoscales, oceans are populated by waves motions and coherent eddies, that contribute actively to transporting matter across ocean basins and from equator to poles. Fine scale processes also comprise *submesoscale* processes, with scale smaller than the first internal Rossby radius (1-20km). At submesoscales, oceans are populated by intense vortices, fronts and filaments, all of which are contributing to vertical exchanges between the ocean interior and the surface, fluxing in particular nutrients from the ocean sub-surface to the sun-lit surface layers where primary production occurs.
```


en indiquant le titre de la nouvelle page, le lien déjà indiqué dans le carousel, et si besoin le lien de la page précédente et suivant et enfin le texte de la page en markdown

  * dans _includes/footer rajouter :


```html
<li> <a href="{{site.baseurl}}/unravel">Exploring ocean fine scales motions</a> </li>
```

en modifiant le titre et le lien de la nouvelle page.

##Rajouter une personne dans la page people :

 * si membre permanent :

   * dans _data/group.yml : rajouter un paragraphe


```html
- name : Thierry Penduff
  title : Head of the Team
  email : penduff.png
  image_nb : Penduff_nb.jpg
  image_color : Penduff_color.jpg
  post : Researcher (CNRS)
  website : http://lgge.osug.fr/personnels/penduff_thierry/FRANCAIS/
  phone : +33 (0) 4 76 82 86 54"
```


dans lequel on indique le nom, si besoin le titre, le nom de l'image qui montre l'adresse mail (à générer avec script email2gif), le nom des photos n&b et couleur, le poste, si besoin l'adresse du site web perso et le numero de téléphone.

   * dans assets/img/people : deposer les photos et l'image de l'adresse mail

  * si membre non-permanent : mêmes manips mais dans le fichier _data/nonperm.yml


##Rajouter un projet dans la liste des projets :

  - dans _data/projects.yml : rajouter un paragraphe


```html
- title : AtlantOS
  image :
  date : 2015-2019
  text : The vision of AtlantOS is to improve and innovate Atlantic observing by using the Framework of Ocean Observing to obtain an international, more sustainable, more efficient, more integrated, and fit-for-purpose system. Hence, the AtlantOS initiative will have a long-lasting and sustainable contribution to the societal, economic and scientific benefit arising from this integrated approach. This will be achieved by improving the value for money, extent, completeness, quality and ease of access to Atlantic Ocean data required by industries, product supplying agencies, scientist and citizens.
  link : https://www.atlantos-h2020.eu/
  ancre : atlantos"
```


dans lequel on indique le titre du projet, si besoin le nom d'une image, les dates du projet, un texte descriptif, un lien et un mot-clé pour désigner le projet (permet de naviguer à l'intérieur de la page)

  - dans _includes/navbar.html : rajouter une ligne


```html
<li><a href="{{site.baseurl}}/projects/nouveau_projet" class={{researchDropdownClass}}>Nouveau Projet</a></li>"
```


permet d'accéder à la page du projet, ou rajouter la ligne


```html
<li><a href="{{site.baseurl}}/projects#ancre" class={{researchDropdownClass}}>Nouveau Projet</a></li>"
```


pour accéder dans la page all projects au paragraphe correspondant au nouveau projet.

##Créer une page projet indépendante (type page SOBUMS) :

  - dans le dossier projects, rajouter un document markdown :


```html
---
layout: pagemd
title: SOBUMS
permalink: /projects/sobums/
---

The Southern Ocean (oceans south of 30°S) plays a key role in global biogeochemical cycles. But large environmental changes are ongoing in the Southern Ocean physical and biogeochemical properties. These changes reflect widespread environmental changes that are occurring throughout the southern hemisphere and over the Southern Ocean (changes in surface winds, solar radiation, sea ice cover and glacial melt from Antarctica). How the Southern Ocean primary production and carbon cycle will respond to these changing climate stressors is a matter of concern in the climate science community.


<img class="img-responsive img-centered" src="https://meom-group.github.io/assets/img/projects/sobums-meijers.png" alt="A changing Southern Ocean."/> "
```


en indiquant le titre du projet, l'adresse de la page et le texte en markdown.

##Rajouter une offre d'emploi :

  - dans jobs.md, ajouter un paragraphe du type :


```html
### PhD grants

 - [Stochastic variability of oceanic water masses](http://www.adum.fr/as/ed/voirproposition.pl?langue=fr&site=edtue&matricule_prop=11736);  contact : Thierry Penduff."
```



##Rajouter une news :

  - dans le dossier _posts, créer un fichier dont le nom commence par la date : year-month-day-title-of-the-news.md et le remplir comme suit : 


```html
---
title: New MEOM website !
featured:
layout: page
link:
---

We are proud to open our new public website today.

Thank to all the team members that contributed to this effort !"
```

en indiquant le titre de la news, une éventuelle image, un éventuel lien et le texte en syntaxe markdown


