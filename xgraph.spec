
Summary:  Interactive plotting and graphing X11 in command line
Name: xgraph
Version: 12.1
Release: 9
License: GPL
Group: Sciences/Mathematics
Source: http://www.isi.edu/nsnam/dist/xgraph-%{version}.tar.gz
Patch0: xgraph-12.1-glibc-2.10.patch
Patch1: xgraph-makefile-gentoo.patch
Patch2: xgraph-12.1-fix-str-fmt.patch
URL: http://www.isi.edu/nsnam/xgraph
BuildRequires: pkgconfig(x11)

%description
The xgraph program draws a graph on an X display given data read from
either data files or from standard input if no files are specified.  It can
display up to 64 independent data sets using different colors and/or line
styles for each set.  It annotates the graph with a title,  axis labels,
grid lines or tick marks, grid labels, and a legend.  There are options to
control the appearance of most components of the graph.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%configure2_5x
%make

%install
rm -rf %_tmppath/%{name}-%{version}-root
%makeinstall_std
mv %{buildroot}%{_mandir}/manm %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/man1/xgraph.man %{buildroot}%{_mandir}/man1/xgraph.1

%files
%doc README* INSTALL examples
%{_bindir}/xgraph
%{_mandir}/man1/xgraph.*

%clean
[ %{buildroot} != "/" ] && rm -fr %{buildroot}



