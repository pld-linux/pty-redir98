Summary:	creates a pair of pseudo-terminals
Summary(pl):	tworzy par� pseudo-terminali
Name:		pty-redir98
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Terminal
Group(de):	Applikationen/Terminal
Group(pl):	Aplikacje/Terminal
Source0:	ftp://ftp.pld.org.pl/software/pty-redir98/%{name}-%{version}.tar.gz
URL:		ftp://ftp.pld.org.pl/software/pty-redir98/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pty-redir98 is a remake of old "pty-redir" application, using Unix98
PTYs. It creates a pair of pseudo-terminals for any application to
use. For example it allows running PPP over SSH by attaching SSH
input/output to a pseudo-tty master and running pppd on corresponding
slave.

%description -l pl
pty-redir98 jest przer�bk� starego programu "pty-redir", u�ywaj�c�
pseudo-terminali zgodnie z semantyk� Unix98. Tworzy par�
pseudo-terminali kt�re dowolna aplikacja mo�e wykorzysta�. Na przyk�ad
umo�liwia uruchomienie PPP po SSH przez podczepienie wej�cia/wyj�cia
SSH do nadrz�dnego pseudo-terminala i uruchomienie pppd na
odpowiadaj�cym mu pseudo-terminalu podrz�dnym.

%prep
%setup -q

%build
rm -f missing
aclocal
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}