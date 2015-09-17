import bleach


def PageCreatorPostProcessing(content):

    processed_content = ''

    # <p>
    paragraphs = ''
    new_content = ''

    tags = ['<h3>', '</h3>', '<ul>', '</ul>', '<li>', '</li>', '<blockquote>', '</blockquote>']

    for double_break in content.split('\r\n\r\n'):

        print "%s - %s" % (double_break, all(tag not in double_break for tag in tags))

        if any(tag not in double_break for tag in tags):
            double_break = '<p>%s</p>\n\n' % double_break

        paragraphs += double_break

    for single_break in paragraphs.split('\r\n'):

        if any(tag not in single_break for tag in tags):
            single_break = '%s<br>\n' % single_break

        new_content += single_break

    processed_content += new_content.rstrip().rstrip('<br>')

    return processed_content


def PageCreatorPreProcessing(content):

    return bleach.clean(content, tags=[None], strip=True)
