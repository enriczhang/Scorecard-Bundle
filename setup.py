import setuptools

# with open("README.md", "r" , encoding='utf-8') as fh:
#     long_description = fh.read()



long_description = '''Scorecard-Bundle is a high-level Scorecard modeling API that is easy-to-use and Scikit-Learn consistent. 
The transformer and model classes in Scorecard-Bundle comply with Scikit-Learn‘s fit-transform-predict 
convention. So far it has covered the key steps in Scorecard modeling, including feature discretization,
feature encoding, feature selection, model training and model evaluation. 
See detailed document at https://github.com/Lantianzz/Scorecard-Bundle 
'''
setuptools.setup(
	name="scorecardbundle",
	version="1.1.3",
	author="Lantian ZHANG",
	author_email="peter.lantian.zhang@outlook.com",
	description="The python scorecard modeling library",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Lantianzz/Scorecard-Bundle",
	classifiers=["Development Status :: 4 - Beta",
				"Intended Audience :: Financial and Insurance Industry",
				"Topic :: Scientific/Engineering :: Artificial Intelligence",
	    		"License :: OSI Approved :: BSD License",		
	    		"Programming Language :: Python :: 3"],
	keywords='Python Scorecard Modeling',
	packages=setuptools.find_packages(exclude=['TEMP','examples']),
	python_requires='>=3.7',
	install_requires=['numpy','scipy','pandas','matplotlib','sklearn'],
)

