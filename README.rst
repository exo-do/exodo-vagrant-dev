Generación entorno de desarrollo exodo/nodebb
----------------------------------------------

- Instala vagrant
- Clona este repositorio en una carpeta, por ejemplo ~/exodo
- Dentro de esta carpeta, ejecuta: ``vagrant up``. Esto tardará en torno a 15 minutos (la primera vez que se ejecute tardará mas tiempo dado que vagrant tiene que descargar la VM. Si todo va bien, al final del proceso deberia haber una carpeta ~/exodo/nodebb.
- Mientras la VM esté functionando, la carpeta ``~/exodo`` estará sincronizada entre el host y el guest. Esto significa que cualquier cambio que hagas se propagará automáticamente a la VM. En ~/exodo/nodebb/node_modules están clonados todos los repositorios de plugins.
- Ejecuta ``vagrant ssh``. Esto abrirá una consola en la VM.
- Muévete a /vagrant/nodebb y ejecuta: ``./nodebb setup``. Esto iniciará el proceso de configuración de nodebb. Ve dandole a intro pero presta atención a cuando te pida la BBDD y escribe ``mongo``. Dale a intro a todo salvo a la creación del administrador. 
- Ejecuta ``./nodebb start`` o ``./nodebb watch``. A partir de este momento nodebb estará funcionando.
- El puerto ``4567`` está sincronizado entre el host y el guest, así que abre tu navegador predilecto y visita la dirección: ``http://localhost:4567``. Esto deberia abrir la portada de nodebb
- Los plugins deben de ser activados manualmente
- Cuando acabes con el desarrollo, apaga la maquina virtual. Para ello ejecuta ``vagrant halt`` o ``vagrant suspend``. El primero apaga la maquina por completo y el segundo la suspende (mas comodo porque no tendrás que arrancar nodebb cada vez)
- Para volver a encender la VM, simplemente ejecuta ``vagrant up``. Si quieres borrarla por completo ``vagrant destroy``.
