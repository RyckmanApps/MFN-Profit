def calculate_profit(user_input):
    """
    This function calculates the net gain and per RO net profit for each insurance carrier based on the user input.
    """
    results = {}

    # Calculate for each insurance carrier
    carriers = ['Allstate', 'Liberty', 'USAA', 'State Farm']
    for carrier in carriers:
        results[carrier] = {}
        carrier_input = user_input[carrier]

        # Calculate Parts Sale
        parts_sale = carrier_input['per_ro_pre_tax_sales'] * carrier_input['parts_sale']

        # Calculate OEM % of parts
        oem_parts = parts_sale * carrier_input['oem_percentage_of_parts']

        # Calculate Parts Discount
        parts_discount = 0
        if carrier_input['parts_disc_apply'] == 1:
            parts_discount = oem_parts * user_input['discount_rate']

        # Calculate BLD Discount
        bld_discount = 0
        if carrier_input['bld_disc_apply'] == 1:
            bld_discount = carrier_input['per_ro_pre_tax_sales'] * 0.025

        # Calculate Total Discounts Given
        total_discounts_given = parts_discount + bld_discount

        # Calculate Total Sales Weight
        total_sales_weight = (carrier_input['per_ro_pre_tax_sales'] * user_input['sample_ro_count'] * carrier_input['ro_count']) / 4

        # Calculate Extrapolated Discount
        extrapolated_discount = total_discounts_given * user_input['sample_ro_count'] * carrier_input['ro_count']

        # Calculate Carrier Incremental Net Profit
        carrier_incremental_net_profit = carrier_input['per_ro_pre_tax_sales'] * carrier_input['ro_count'] * user_input['net_p']

        # Calculate Net Gain
        net_gain = carrier_incremental_net_profit - extrapolated_discount

        # Calculate Per RO Net Profit
        per_ro_net_profit = net_gain / carrier_input['ro_count']

        # Store results
        results[carrier]['net_gain'] = net_gain
        results[carrier]['per_ro_net_profit'] = per_ro_net_profit

    return results
