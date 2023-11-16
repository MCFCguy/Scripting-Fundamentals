# Write your function here
def resources_scanner(package):
    resources = dir(package)
    resources.insert(3, "_TemplateMetaclass")
    for item in resources:
        print(item)

if __name__ == '__main__':
    import string 
    resources_scanner(string)
