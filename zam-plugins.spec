#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : zam-plugins
Version  : 3.14
Release  : 209
URL      : file:///aot/build/clearlinux/packages/zam-plugins/zam-plugins-v3.14.tar.gz
Source0  : file:///aot/build/clearlinux/packages/zam-plugins/zam-plugins-v3.14.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-dev32
BuildRequires : autogen
BuildRequires : autogen-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : binutils-dev
BuildRequires : binutils-extras
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : clr-rpm-config
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : dejagnu
BuildRequires : docbook-utils
BuildRequires : docbook-xml
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : expect
BuildRequires : fftw-dev
BuildRequires : fftw-staticdev
BuildRequires : findutils
BuildRequires : flac
BuildRequires : flac-dev
BuildRequires : flac-dev32
BuildRequires : flac-staticdev
BuildRequires : flac-staticdev32
BuildRequires : flex
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-go
BuildRequires : gcc-go-lib
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb-dev
BuildRequires : git
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-doc
BuildRequires : glibc-extras
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : glibc-nscd
BuildRequires : glibc-staticdev
BuildRequires : glibc-utils
BuildRequires : gmp-dev
BuildRequires : googletest-dev
BuildRequires : graphviz
BuildRequires : gtk+-dev
BuildRequires : guile
BuildRequires : ladspa_sdk
BuildRequires : ladspa_sdk-dev
BuildRequires : ladspa_sdk-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : liblo
BuildRequires : liblo-dev
BuildRequires : liblo-staticdev
BuildRequires : libogg-dev
BuildRequires : libogg-dev32
BuildRequires : libogg-staticdev
BuildRequires : libogg-staticdev32
BuildRequires : libpng-dev
BuildRequires : libpng-staticdev
BuildRequires : libsamplerate-dev
BuildRequires : libsamplerate-staticdev
BuildRequires : libsndfile-dev
BuildRequires : libsndfile-staticdev
BuildRequires : libstdc++
BuildRequires : libtool-dev
BuildRequires : libunwind-dev
BuildRequires : libvorbis-dev
BuildRequires : libvorbis-dev32
BuildRequires : libvorbis-staticdev
BuildRequires : libvorbis-staticdev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : lv2
BuildRequires : lv2-dev
BuildRequires : mesa
BuildRequires : mesa-dev
BuildRequires : meson
BuildRequires : mpc-dev
BuildRequires : mpfr-dev
BuildRequires : ncurses
BuildRequires : ncurses-dev
BuildRequires : ninja
BuildRequires : octave-dev
BuildRequires : opus
BuildRequires : opus-dev
BuildRequires : opus-lib
BuildRequires : opus-staticdev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pcre2-dev
BuildRequires : pcre2-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(lv2)
BuildRequires : pkgconfig(rubberband)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : procps-ng
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : rdflib
BuildRequires : sed
BuildRequires : serd
BuildRequires : serd-dev
BuildRequires : serd-staticdev
BuildRequires : sord
BuildRequires : sord-dev
BuildRequires : sord-staticdev
BuildRequires : speex-dev
BuildRequires : speex-staticdev
BuildRequires : speexdsp-dev
BuildRequires : speexdsp-staticdev
BuildRequires : sqlite-autoconf-dev
BuildRequires : sratom
BuildRequires : sratom-dev
BuildRequires : sratom-staticdev
BuildRequires : tcl
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : valgrind-dev
BuildRequires : vamp-sdk
BuildRequires : vamp-sdk-dev
BuildRequires : vamp-sdk-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zita-convolver
BuildRequires : zita-convolver-dev
BuildRequires : zita-convolver-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
zam-plugins [![travis](https://travis-ci.org/zamaudio/zam-plugins.svg?branch=master)](https://travis-ci.org/zamaudio/zam-plugins)
===========

%package dev
Summary: dev components for the zam-plugins package.
Group: Development
Provides: zam-plugins-devel = %{version}-%{release}
Requires: zam-plugins = %{version}-%{release}

%description dev
dev components for the zam-plugins package.


%prep
%setup -q -n zam-plugins-clr
cd %{_builddir}/zam-plugins-clr

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640216102
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1f content
## altflags1
export HAVE_ZITA_CONVOLVER=true
unset ASFLAGS
export CFLAGS="-g3 -ggdb -Ofast -fdata-sections -ffunction-sections --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export ASMFLAGS="-g3 -ggdb -Ofast -fdata-sections -ffunction-sections --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CXXFLAGS="-g3 -ggdb -Ofast -fdata-sections -ffunction-sections --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FCFLAGS="-g3 -ggdb -Ofast -fdata-sections -ffunction-sections --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g3 -ggdb -Ofast -fdata-sections -ffunction-sections --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CFFLAGS="-g3 -ggdb -Ofast -fdata-sections -ffunction-sections --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export LDFLAGS="-g3 -ggdb -Ofast -fdata-sections -ffunction-sections --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
## altflags1f end
make  %{?_smp_mflags}   USE_SYSTEM_LIBS=1 SKIP_STRIPPING=true HAVE_ZITA_CONVOLVER=true VERBOSE=true HAVE_DGL=false HAVE_CAIRO=false HAVE_OPENGL=false V=1 VERBOSE=1


%install
export SOURCE_DATE_EPOCH=1640216102
rm -rf %{buildroot}
%make_install USE_SYSTEM_LIBS=1 SKIP_STRIPPING=true HAVE_ZITA_CONVOLVER=true VERBOSE=true HAVE_DGL=false HAVE_CAIRO=false HAVE_OPENGL=false

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/ladspa/ZaMaximX2-ladspa.so
/usr/lib64/ladspa/ZaMultiComp-ladspa.so
/usr/lib64/ladspa/ZaMultiCompX2-ladspa.so
/usr/lib64/ladspa/ZamAutoSat-ladspa.so
/usr/lib64/ladspa/ZamComp-ladspa.so
/usr/lib64/ladspa/ZamCompX2-ladspa.so
/usr/lib64/ladspa/ZamDelay-ladspa.so
/usr/lib64/ladspa/ZamDynamicEQ-ladspa.so
/usr/lib64/ladspa/ZamEQ2-ladspa.so
/usr/lib64/ladspa/ZamGEQ31-ladspa.so
/usr/lib64/ladspa/ZamGate-ladspa.so
/usr/lib64/ladspa/ZamGateX2-ladspa.so
/usr/lib64/ladspa/ZamGrains-ladspa.so
/usr/lib64/ladspa/ZamPhono-ladspa.so
/usr/lib64/ladspa/ZamTube-ladspa.so
/usr/lib64/lv2/ZaMaximX2.lv2/ZaMaximX2_dsp.so
/usr/lib64/lv2/ZaMaximX2.lv2/ZaMaximX2_dsp.ttl
/usr/lib64/lv2/ZaMaximX2.lv2/manifest.ttl
/usr/lib64/lv2/ZaMaximX2.lv2/presets.ttl
/usr/lib64/lv2/ZaMultiComp.lv2/ZaMultiComp_dsp.so
/usr/lib64/lv2/ZaMultiComp.lv2/ZaMultiComp_dsp.ttl
/usr/lib64/lv2/ZaMultiComp.lv2/manifest.ttl
/usr/lib64/lv2/ZaMultiComp.lv2/presets.ttl
/usr/lib64/lv2/ZaMultiCompX2.lv2/ZaMultiCompX2_dsp.so
/usr/lib64/lv2/ZaMultiCompX2.lv2/ZaMultiCompX2_dsp.ttl
/usr/lib64/lv2/ZaMultiCompX2.lv2/manifest.ttl
/usr/lib64/lv2/ZaMultiCompX2.lv2/presets.ttl
/usr/lib64/lv2/ZamAutoSat.lv2/ZamAutoSat_dsp.so
/usr/lib64/lv2/ZamAutoSat.lv2/ZamAutoSat_dsp.ttl
/usr/lib64/lv2/ZamAutoSat.lv2/manifest.ttl
/usr/lib64/lv2/ZamComp.lv2/ZamComp_dsp.so
/usr/lib64/lv2/ZamComp.lv2/ZamComp_dsp.ttl
/usr/lib64/lv2/ZamComp.lv2/manifest.ttl
/usr/lib64/lv2/ZamComp.lv2/presets.ttl
/usr/lib64/lv2/ZamCompX2.lv2/ZamCompX2_dsp.so
/usr/lib64/lv2/ZamCompX2.lv2/ZamCompX2_dsp.ttl
/usr/lib64/lv2/ZamCompX2.lv2/manifest.ttl
/usr/lib64/lv2/ZamCompX2.lv2/presets.ttl
/usr/lib64/lv2/ZamDelay.lv2/ZamDelay_dsp.so
/usr/lib64/lv2/ZamDelay.lv2/ZamDelay_dsp.ttl
/usr/lib64/lv2/ZamDelay.lv2/manifest.ttl
/usr/lib64/lv2/ZamDelay.lv2/presets.ttl
/usr/lib64/lv2/ZamDynamicEQ.lv2/ZamDynamicEQ_dsp.so
/usr/lib64/lv2/ZamDynamicEQ.lv2/ZamDynamicEQ_dsp.ttl
/usr/lib64/lv2/ZamDynamicEQ.lv2/manifest.ttl
/usr/lib64/lv2/ZamDynamicEQ.lv2/presets.ttl
/usr/lib64/lv2/ZamEQ2.lv2/ZamEQ2_dsp.so
/usr/lib64/lv2/ZamEQ2.lv2/ZamEQ2_dsp.ttl
/usr/lib64/lv2/ZamEQ2.lv2/manifest.ttl
/usr/lib64/lv2/ZamEQ2.lv2/presets.ttl
/usr/lib64/lv2/ZamGEQ31.lv2/ZamGEQ31_dsp.so
/usr/lib64/lv2/ZamGEQ31.lv2/ZamGEQ31_dsp.ttl
/usr/lib64/lv2/ZamGEQ31.lv2/manifest.ttl
/usr/lib64/lv2/ZamGEQ31.lv2/presets.ttl
/usr/lib64/lv2/ZamGate.lv2/ZamGate_dsp.so
/usr/lib64/lv2/ZamGate.lv2/ZamGate_dsp.ttl
/usr/lib64/lv2/ZamGate.lv2/manifest.ttl
/usr/lib64/lv2/ZamGate.lv2/presets.ttl
/usr/lib64/lv2/ZamGateX2.lv2/ZamGateX2_dsp.so
/usr/lib64/lv2/ZamGateX2.lv2/ZamGateX2_dsp.ttl
/usr/lib64/lv2/ZamGateX2.lv2/manifest.ttl
/usr/lib64/lv2/ZamGateX2.lv2/presets.ttl
/usr/lib64/lv2/ZamGrains.lv2/ZamGrains_dsp.so
/usr/lib64/lv2/ZamGrains.lv2/ZamGrains_dsp.ttl
/usr/lib64/lv2/ZamGrains.lv2/manifest.ttl
/usr/lib64/lv2/ZamGrains.lv2/presets.ttl
/usr/lib64/lv2/ZamHeadX2.lv2/ZamHeadX2_dsp.so
/usr/lib64/lv2/ZamHeadX2.lv2/ZamHeadX2_dsp.ttl
/usr/lib64/lv2/ZamHeadX2.lv2/manifest.ttl
/usr/lib64/lv2/ZamHeadX2.lv2/presets.ttl
/usr/lib64/lv2/ZamPhono.lv2/ZamPhono_dsp.so
/usr/lib64/lv2/ZamPhono.lv2/ZamPhono_dsp.ttl
/usr/lib64/lv2/ZamPhono.lv2/manifest.ttl
/usr/lib64/lv2/ZamPhono.lv2/presets.ttl
/usr/lib64/lv2/ZamTube.lv2/ZamTube_dsp.so
/usr/lib64/lv2/ZamTube.lv2/ZamTube_dsp.ttl
/usr/lib64/lv2/ZamTube.lv2/manifest.ttl
/usr/lib64/lv2/ZamTube.lv2/presets.ttl
/usr/lib64/lv2/ZamVerb.lv2/ZamVerb_dsp.so
/usr/lib64/lv2/ZamVerb.lv2/ZamVerb_dsp.ttl
/usr/lib64/lv2/ZamVerb.lv2/manifest.ttl
/usr/lib64/lv2/ZamVerb.lv2/presets.ttl
/usr/lib64/vst/ZaMaximX2-vst.so
/usr/lib64/vst/ZaMultiComp-vst.so
/usr/lib64/vst/ZaMultiCompX2-vst.so
/usr/lib64/vst/ZamAutoSat-vst.so
/usr/lib64/vst/ZamComp-vst.so
/usr/lib64/vst/ZamCompX2-vst.so
/usr/lib64/vst/ZamDelay-vst.so
/usr/lib64/vst/ZamDynamicEQ-vst.so
/usr/lib64/vst/ZamEQ2-vst.so
/usr/lib64/vst/ZamGEQ31-vst.so
/usr/lib64/vst/ZamGate-vst.so
/usr/lib64/vst/ZamGateX2-vst.so
/usr/lib64/vst/ZamGrains-vst.so
/usr/lib64/vst/ZamHeadX2-vst.so
/usr/lib64/vst/ZamPhono-vst.so
/usr/lib64/vst/ZamTube-vst.so
/usr/lib64/vst/ZamVerb-vst.so
