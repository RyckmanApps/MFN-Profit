def handle_input():
    """
    This function will handle user input. It will prompt the user to enter the necessary information and then return that information in a dictionary.
    """
    user_input = {}

    # Get user input for each insurance carrier
    carriers = ['Allstate', 'Liberty', 'USAA', 'State Farm']
    for carrier in carriers:
        user_input[carrier] = {}
        user_input[carrier]['is_drp'] = int(input(f"Is {carrier} a DRP? Enter 1 for Yes and 0 for No: "))
        user_input[carrier]['per_ro_pre_tax_sales'] = float(input(f"Enter the Per-RO Pre-Tax Sales for {carrier}: "))
        user_input[carrier]['parts_sale'] = float(input(f"Enter the Parts Sale for {carrier}: "))
        user_input[carrier]['oem_percentage_of_parts'] = float(input(f"Enter the OEM % of parts for {carrier}: "))
        user_input[carrier]['parts_disc_apply'] = int(input(f"Does Parts Discount Apply for {carrier}? Enter 1 for Yes and 0 for No: "))
        user_input[carrier]['bld_disc_apply'] = int(input(f"Does BLD Discount Apply for {carrier}? Enter 1 for Yes and 0 for No: "))
        user_input[carrier]['ro_count'] = int(input(f"Enter the RO Count for {carrier}: "))
        user_input[carrier]['volume_share'] = float(input(f"Enter the Volume Share for {carrier}: "))

    # Get user input for general parameters
    user_input['foreign_domestic'] = int(input("Enter 1 for Foreign and 0 for Domestic: "))
    user_input['discount_rate'] = float(input("Enter the Discount Rate: "))
    user_input['sample_ro_count'] = int(input("Enter the Sample RO Count: "))
    user_input['net_p'] = float(input("Enter the Net P%: "))

    return user_input
