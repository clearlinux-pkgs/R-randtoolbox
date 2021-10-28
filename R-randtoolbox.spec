#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-randtoolbox
Version  : 1.31.0
Release  : 28
URL      : https://cran.r-project.org/src/contrib/randtoolbox_1.31.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/randtoolbox_1.31.0.tar.gz
Summary  : Toolbox for Pseudo and Quasi Random Number Generation and Random
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-randtoolbox-lib = %{version}-%{release}
Requires: R-rngWELL
BuildRequires : R-rngWELL
BuildRequires : buildreq-R

%description
multiple recursive generators and generalized feedback shift register (SF-Mersenne Twister
    algorithm and WELL generators); (2) quasi random generators - the Torus algorithm, the
    Sobol sequence, the Halton sequence (including the Van der Corput sequence) and (3) some
    generator tests - the gap test, the serial test, the poker test.

%package lib
Summary: lib components for the R-randtoolbox package.
Group: Libraries

%description lib
lib components for the R-randtoolbox package.


%prep
%setup -q -c -n randtoolbox
cd %{_builddir}/randtoolbox

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635379303

%install
export SOURCE_DATE_EPOCH=1635379303
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randtoolbox
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randtoolbox
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randtoolbox
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc randtoolbox || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/randtoolbox/CITATION
/usr/lib64/R/library/randtoolbox/DESCRIPTION
/usr/lib64/R/library/randtoolbox/INDEX
/usr/lib64/R/library/randtoolbox/LICENSE
/usr/lib64/R/library/randtoolbox/Meta/Rd.rds
/usr/lib64/R/library/randtoolbox/Meta/features.rds
/usr/lib64/R/library/randtoolbox/Meta/hsearch.rds
/usr/lib64/R/library/randtoolbox/Meta/links.rds
/usr/lib64/R/library/randtoolbox/Meta/nsInfo.rds
/usr/lib64/R/library/randtoolbox/Meta/package.rds
/usr/lib64/R/library/randtoolbox/Meta/vignette.rds
/usr/lib64/R/library/randtoolbox/NAMESPACE
/usr/lib64/R/library/randtoolbox/NEWS
/usr/lib64/R/library/randtoolbox/R/randtoolbox
/usr/lib64/R/library/randtoolbox/R/randtoolbox.rdb
/usr/lib64/R/library/randtoolbox/R/randtoolbox.rdx
/usr/lib64/R/library/randtoolbox/doc/fullpres.R
/usr/lib64/R/library/randtoolbox/doc/fullpres.Rnw
/usr/lib64/R/library/randtoolbox/doc/fullpres.pdf
/usr/lib64/R/library/randtoolbox/doc/index.html
/usr/lib64/R/library/randtoolbox/doc/shortintro.R
/usr/lib64/R/library/randtoolbox/doc/shortintro.Rnw
/usr/lib64/R/library/randtoolbox/doc/shortintro.pdf
/usr/lib64/R/library/randtoolbox/help/AnIndex
/usr/lib64/R/library/randtoolbox/help/aliases.rds
/usr/lib64/R/library/randtoolbox/help/paths.rds
/usr/lib64/R/library/randtoolbox/help/randtoolbox.rdb
/usr/lib64/R/library/randtoolbox/help/randtoolbox.rdx
/usr/lib64/R/library/randtoolbox/html/00Index.html
/usr/lib64/R/library/randtoolbox/html/R.css
/usr/lib64/R/library/randtoolbox/tests/test-SFMT.R
/usr/lib64/R/library/randtoolbox/tests/test-parallel-qmc.R
/usr/lib64/R/library/randtoolbox/tests/test-permut.R
/usr/lib64/R/library/randtoolbox/tests/test-runifInterface-LCG.R
/usr/lib64/R/library/randtoolbox/tests/test-runifInterface-nonLCG.R
/usr/lib64/R/library/randtoolbox/tests/test-sobol-Ccode.R
/usr/lib64/R/library/randtoolbox/tests/test-sobol-basic.R
/usr/lib64/R/library/randtoolbox/tests/test-sobol-scram.R
/usr/lib64/R/library/randtoolbox/tests/testHalton.R
/usr/lib64/R/library/randtoolbox/tests/testSobol.R
/usr/lib64/R/library/randtoolbox/tests/testStirling.R
/usr/lib64/R/library/randtoolbox/tests/testTorus.R
/usr/lib64/R/library/randtoolbox/tests/testWELL.R
/usr/lib64/R/library/randtoolbox/tests/testenvir.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/randtoolbox/libs/randtoolbox.so
/usr/lib64/R/library/randtoolbox/libs/randtoolbox.so.avx2
/usr/lib64/R/library/randtoolbox/libs/randtoolbox.so.avx512
