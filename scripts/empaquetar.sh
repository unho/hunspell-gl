#!/bin/bash

rootFolder="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
code="gl_ES"
version="$1"
if [ -z "$1" ]; then
	version="$(date -u +"%Y%m%d")"
fi

pushd $rootFolder &> /dev/null

# Eliminar o cartafol de construción existente se o hai.
rm -rf ./build

# Construír e empaquetar o corrector principal (VOLG).
scons aff=norma dic=volga rep=comunidade,galipedia code=${code}
pushd build &> /dev/null
packageName="hunspell-gl-volg-${version}"
mkdir ${packageName}
mv ${code}.aff ${packageName}/${code}.aff
mv ${code}.dic ${packageName}/${code}.dic
for filename in $(find .. -name "*.txt")
do
  cp "$filename" "${packageName}/"
done
tar -cavf ${packageName}.tar.xz ${packageName} &> /dev/null
mv ${packageName}.tar.xz ../${packageName}.tar.xz
popd &> /dev/null

# Construír e empaquetar o corrector da comunidade.
scons aff=norma,trasno,unidades dic=comunidade,galipedia,iso639,iso4217,trasno,unidades,volga rep=comunidade,galipedia code=${code}
pushd build &> /dev/null
packageName="hunspell-gl-comunidade-${version}"
mkdir ${packageName}
mv ${code}.aff ${packageName}/${code}.aff
mv ${code}.dic ${packageName}/${code}.dic
for filename in $(find .. -name "*.txt")
do
  cp "$filename" "${packageName}/"
done
tar -cavf ${packageName}.tar.xz ${packageName} &> /dev/null
mv ${packageName}.tar.xz ../${packageName}.tar.xz
popd &> /dev/null

# Empaquetar todas as fontes.
mkdir -p build
pushd build &> /dev/null
packageName="hunspell-gl-fontes-${version}"
mkdir ${packageName}
for folder in scripts src
do
	cp -R ../${folder} ${packageName}/${folder}
done
for filename in $(find .. -name "*.txt") ../builds ../SConstruct
do
  cp "$filename" "${packageName}/"
done
tar -cavf ${packageName}.tar.xz ${packageName} &> /dev/null
mv ${packageName}.tar.xz ../${packageName}.tar.xz
popd &> /dev/null

# Eliminar o cartafol de construción.
rm -rf ./build

popd &> /dev/null
