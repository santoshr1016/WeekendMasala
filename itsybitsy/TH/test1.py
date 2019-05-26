def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    print(keyvals)
    print(attr_str)

make_element('item', 'Albatross', size='large', quantity=6)
