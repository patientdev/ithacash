import bleach

def PageCreatorBleaching(flatpage_content):

    bleach.ALLOWED_TAGS.extend(['p', 'mark', 'h3', 'h4', 'br', 'img', 'input', 'button'])
    bleach.ALLOWED_ATTRIBUTES['a'].extend(['class', 'target'])
    bleach.ALLOWED_ATTRIBUTES['img'] = ['src', 'height', 'width']
    bleach.ALLOWED_ATTRIBUTES['input'] = ['type', 'id', 'name', 'value', 'placeholder']
    bleach.ALLOWED_ATTRIBUTES['form'] = ['id', 'action']

    bleached_content = bleach.clean(flatpage.content, tags=bleach.ALLOWED_TAGS, attributes=bleach.ALLOWED_ATTRIBUTES, strip=True)

    return bleached_content
