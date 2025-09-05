#!/usr/bin/sh

# Define diretorio dos artefatos zip para os lambdas
DIR_ARTIFACTS="infra/artifacts"
if [ ! -d $DIR_ARTIFACTS ]; then mkdir -p $DIR_ARTIFACTS; fi

# Lista aplicações lambda
LISTA_APPS=$(ls -d app/mmt/*/)
cd app

for FULL_DIR_APP in $LISTA_APPS; do
    
    DIR_APP=$(basename "$FULL_DIR_APP")
    
    echo "Limpando $DIR_APP ..."
    rm -rf $DIR_APP/__pycache__
    rm -rf $DIR_APP/*.pyc
    rm -rf $DIR_APP/.pytest_cache

    echo "Removendo ZIP antigo de $DIR_APP ..."
    if [ -f $DIR_ARTIFACTS/$DIR_APP.zip ]; then rm $DIR_ARTIFACTS/$DIR_APP.zip; fi
    
    echo "Gerando ZIP para $DIR_APP ..."
    zip -r ../$DIR_ARTIFACTS/$DIR_APP.zip mmt/$DIR_APP/ mmt/__init__.py > /dev/null
done

cd ..
echo "Artefatos gerados em $DIR_ARTIFACTS"
ls -lh $DIR_ARTIFACTS