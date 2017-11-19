%global srcname hypothesis

Name:           python-%{srcname}
Version:        3.38.0
Release:        1%{?dist}
Summary:        Library for property based testing

License:        MPLv2.0
URL:            https://github.com/HypothesisWorks/hypothesis-python
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# disable Sphinx extensions that require Internet access
Patch0:         %{srcname}-3.12.0-offline.patch

# Manpage
BuildRequires:  %{_bindir}/sphinx-build

BuildArch:      noarch

%global _description \
Hypothesis is a library for testing your Python code against a much\
larger range of examples than you would ever want to write by\
hand. It’s based on the Haskell library, Quickcheck, and is designed\
to integrate seamlessly into your existing Python unit testing work\
flow.

%description %{_description}

%package     -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-attrs
BuildRequires:  python2-coverage
BuildRequires:  python2-enum34
%{?python_provide:%python_provide python2-%{srcname}}
Requires:       python2-attrs
Requires:       python2-coverage
Requires:       python2-enum34
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Suggests:       python2-numpy
Suggests:       python2-pytz
%endif

%description -n python2-%{srcname} %{_description}

Python 2 version.

%package     -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-attrs
BuildRequires:  python3-coverage
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-attrs
Requires:       python3-coverage
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Suggests:       python3-numpy
Suggests:       python3-pytz
%endif
Obsoletes:      platform-python-%{srcname} < %{version}-%{release}

%description -n python3-%{srcname} %{_description}

Python 2 version.

%prep
%autosetup -n %{srcname}-python-%{version} -p1

%build
%py2_build
%py3_build
PYTHONPATH=src READTHEDOCS=True sphinx-build -b man docs docs/_build/man

%install
%py2_install
%py3_install

%{__install} -Dp -m 644 docs/_build/man/hypothesis.1 \
             $RPM_BUILD_ROOT%{_mandir}/man1/hypothesis.1

%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/hypothesis-*.egg-info/
%{python2_sitelib}/hypothesis/
%{_mandir}/man1/hypothesis.1*

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/hypothesis-*.egg-info
%{python3_sitelib}/hypothesis/
%{_mandir}/man1/hypothesis.1*

%changelog
* Sun Nov 19 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.38.0-1
- Update to 3.38.0

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.37.0-1
- Update to 3.37.0

* Sun Nov 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.36.1-1
- Update to 3.36.1

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.36.0-2
- Use better Obsoletes for platform-python

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.36.0-1
- Update to 3.36.0

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.34.1-1
- Update to 3.34.1

* Sat Nov 04 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.34.0-1
- Update to 3.34.0

* Thu Nov 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.33.1-1
- Update to 3.33.1

* Thu Aug 24 2017 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-4
- Rebuilt for rhbz#1484607

* Thu Aug 10 2017 Tomas Orsava <torsava@redhat.com> - 3.12.0-3
- Added the platform-python subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.12.0-1
- Update to 3.12.0
- Reenable docs in EPEL7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 29 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Version the explicit Provides

* Wed May 04 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.1.3-1
- Update to 3.1.3
- Remove unused code
- Remove unused dependencies

* Sun Feb 14 2016 Michel Salim <salimma@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Michel Salim <salimma@fedoraproject.org> - 1.11.2-1
- Update to 1.11.2

* Sun Sep 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Wed Sep  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-3
- Re-disable tests for now

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-2
- Disable Python3 tests - need debugging on ARM builders

* Mon Aug 31 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-1
- Update to 1.10.6
- Enable tests

* Fri Aug  7 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.0-1
- Update to 1.10

* Wed Jul 29 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-2
- Remove she-bang from tools/mergedbs.py
- Include manpage

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5
- Make Python3 build unconditional

* Thu Jul 23 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.2-1
- Initial package
