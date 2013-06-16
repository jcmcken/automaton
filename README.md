# Automaton

A command-line utility that runs Puppet classes as scripts.

``automaton`` is a just a light wrapper around various other tools that provides a simplified interface
for running Puppet classes as if they were scripts.

## Requirements

* Puppet ``>= 3``
* Hiera
* JGen (<https://github.com/jcmcken/jgen>)

## Examples

The following run...

```bash
[jcmcken@localhost]$ automaton bootstrap::puppetmaster ca=false ca_server=foo.bar.com
```

...does the following:

* Generates a temporary Hiera configuration file containing YAML generated through the ``jgen`` utility.
  That data looks like the following:

```yaml
---
bootstrap::puppetmaster::ca: false
bootstrap::puppetmaster::ca_server: foo.bar.com
```

* Executes a ``puppet apply``, relying on Puppet 3's automatic Hiera lookup for parameterized classes, 
  against the generated Hiera data.

## Why?

Because running stuff like this...

```bash
[jcmcken@localhost]$ cat << EOF | puppet apply
class {'bootstrap::puppetmaster':
  ca        => false,
  ca_server => 'foo.bar.com',
}
EOF
```

...is annoying.

I wanted a simple, easy way to pass parameters to a parameterized class via ``puppet apply``.
