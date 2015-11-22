awallet2keepassx
================

Converts CSV files exported from [aWallet](https://play.google.com/store/apps/details?id=org.awallet.free) to XML to be imported by [KeePassX](https://www.keepassx.org/) and then used by [KeePassDroid](https://play.google.com/store/apps/details?id=com.android.keepass).

Usage
-----

Typical usage:

```
python awallet2keepassx.py dir out.xml
```

With *dir* being the directory that contains the CSV files that got exported from the aWallet Android app and *out.xml* the XML in KeePassX format to be created.
