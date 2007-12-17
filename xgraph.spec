%define version 12.1
%define release %mkrel 3

Summary:  Interactive plotting and graphing X11 in command line
Name: xgraph
Version: %version
Release: %release
License: GPL
Group: Sciences/Mathematics
Source: http://www.isi.edu/nsnam/dist/xgraph-%version.tar.bz2
URL: http://www.isi.edu/nsnam/xgraph

BuildRequires: X11-devel

%description
The xgraph program draws a graph on an X display given data read from
either data files or from standard input if no files are specified.  It can
display up to 64 independent data sets using different colors and/or line
styles for each set.  It annotates the graph with a title,  axis labels,
grid lines or tick marks, grid labels, and a legend.  There are options to
control the appearance of most components of the graph.

%prep
%setup -q 

%build
%configure 
%make

%install
rm -rf %_tmppath/%name-%version-root
%makeinstall
mv %buildroot%{_mandir}/manm %buildroot%{_mandir}/man1
mv %buildroot%{_mandir}/man1/xgraph.man %buildroot%{_mandir}/man1/xgraph.1

%files
%defattr(-,root,root)
%doc README* INSTALL examples
%{_bindir}/xgraph
%{_mandir}/man1/xgraph.*

%clean
[ %buildroot != "/" ] && rm -fr %buildroot

