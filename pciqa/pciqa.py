from file import make_binder


def main():
    make_binder()

    def test_checkboxes():
        """
        Runs all the functions in the checkboxes.py file

            Rather than explicitly call every function, this is a way to run all the functions in the file.
            This way we don't have to remember to add new functions to the test suite.
        """
        import checkboxes
        for i in dir(checkboxes):
            item = getattr(checkboxes,i)
            if callable(item):
                item()
    test_checkboxes()

    '''
        def test_dates():
            pass

        def test_content():
            pass

        def test_writeup():
            pass

        def test_evidence():
            
        '''
if __name__ == '__main__':
    main()
